import pandas as pd

pd.options.mode.chained_assignment = 'raise'

# 此项目使用 Python 3.12 开发，使用了较新规范的类型标注（Type Hints）
# 使用 Python 3.11 及以下版本的 Python 运行需要删除代码中所有的类型标注


""" 任务一
简介：
根据“城市疫情”工作表中的数据统计每日累计确诊人数、累计治愈
人数和累计死亡人数输出武汉、南阳每月 10、25日的统计结果。

要求：
结果包含城市、日期、累计确诊人数、累计治愈人数、累计死亡人
数等数据。将结果保存到“国内新冠疫情数据统计结果.xlsx”文件
中, 工作表名为“城市疫情”。

表格：
日期, 城市, 新增确诊, 新增治愈, 新增死亡
"""


# 从 excel 表的 "城市疫情" 工作表读取数据
全国数据 = pd.read_excel('./新冠疫情分析数据.xlsx', sheet_name='城市疫情')
# 删除无效值的行
全国数据.dropna(axis=0, inplace=True)
# 把 日期列 从字符串类型转换为 TimestampSeries
全国数据['日期'] = pd.to_datetime(全国数据['日期'])
# 按照 城市列 对 "全国数据" 进行分组并存储到 "城市数据"
城市数据 = 全国数据.groupby(by='城市')


def 添加累计确诊治愈死亡数据(城市数据: pd.DataFrame):
  """
  此函数会对传入的数据按日期进行排序！！！

  此函数通过引用传递修改原始数据！！！

  请传入原始的 DataFrame 或在传递参数时调用 DataFrame.copy() 方法。
  否则将会触发 SettingWithCopyWarning 异常。
  """

  # 按照日期列进行排序，默认 ASC
  城市数据.sort_values(by='日期', inplace=True)
  # 计算列 新增确诊 的累加值，并将其存储到列 累计确诊
  城市数据['累计确诊'] = 城市数据['新增确诊'].cumsum()
  # 计算列 新增治愈 的累加值，并将其存储到列 累计治愈
  城市数据['累计治愈'] = 城市数据['新增治愈'].cumsum()
  # 计算列 新增死亡 的累加值，并将其存储到列 累计死亡
  城市数据['累计死亡'] = 城市数据['新增死亡'].cumsum()


def 补全缺失的日期数据(城市数据: pd.DataFrame, 填充列: list[str] = [], 填充值: any = None, 缺省列: list[str] = []) -> pd.DataFrame:
  """
  因为 DataFrame.reindex() 返回了一个新的 DataFrame
  所以此函数只能返回一个新的 DataFrame, 而不是通过引用传递修改原始数据。
  """

  # 根据城市数据的最小日期和最大日期生成日期序列，以天为单位递增
  日期范围 = pd.date_range(start=城市数据['日期'].min(), end=城市数据['日期'].max(), freq='D')
  # 将日期列设置为索引列
  城市数据.set_index('日期', inplace=True)
  # 使用可选填充逻辑使城市数据符合新索引
  城市数据 = 城市数据.reindex(index=日期范围, fill_value=None)
  # 重置索引
  城市数据.reset_index(inplace=True)
  # 对于根据日期补全的行，新增确诊、新增治愈、新增死亡列为 0
  for 列名 in 填充列:
    城市数据[列名].fillna(填充值, inplace=True)
  # 对于根据日期补全的行，某些列需要从有效数据的列复制
  城市数据[缺省列] = 城市数据[缺省列].ffill()

  return 城市数据


# 在代码中为什么使用 pd.DataFrame() 创建副本而不是通过 DataFrame.copy()？
# 因为 DataFrameGroupBy.get_group() 函数的返回值类型是 Any。
# 这意味着 pandas 并不知道数据分组后其中某一组的数据类型。
# 调用 Any.copy() 是非常危险的，因为 Any 可以是任何东西。
# 复制 DataFrame 的时使用 pd.DataFrame() 对于 IDE 来讲是安全的。
# 至于为什么安全，你可能就需要看看 DataFrame 类的构造器是如何实现的了


武汉 = pd.DataFrame(城市数据.get_group('武汉'))
添加累计确诊治愈死亡数据(武汉)
武汉 = 补全缺失的日期数据(
  武汉,
  填充列=['累计确诊', '累计治愈', '累计死亡'],
  填充值=0,
  缺省列=['城市', '累计确诊', '累计治愈', '累计死亡']
)
武汉 = 武汉[武汉['index'].dt.day.isin((10, 25))]
print(武汉, end='\n\n')


南阳 = pd.DataFrame(城市数据.get_group('南阳'))
添加累计确诊治愈死亡数据(南阳)
南阳 = 补全缺失的日期数据(
  南阳,
  填充列=['累计确诊', '累计治愈', '累计死亡'],
  填充值=0,
  缺省列=['城市', '累计确诊', '累计治愈', '累计死亡']
)
南阳 = 南阳[南阳['index'].dt.day.isin((10, 25))]
print(南阳)


""" 任务二
简介：
根据任务1结果, 结合 “城市省份对照表”统计各省级行政单位
按日新增和累计数据输出湖北、广东每月 15 日的统计结果。

要求：
结果包含省份、日期、新增确诊人数、新增治愈人数、新增死亡
人数、累计确诊人数、累计治愈人数、累计死亡人数等数据。
"""


# 从 excel 表的 "城市省份对照表" 工作表读取数据
城市省份对照表 = pd.read_excel('./新冠疫情分析数据.xlsx', sheet_name='城市省份对照表')
# 将城市省份对照表合并到全国数据内
全国数据: pd.DataFrame = 全国数据.merge(城市省份对照表, on='城市')
# 按省份对全国数据进行分组
省份数据 = 全国数据.groupby(by='省份')

# 复制湖北省的数据
湖北 = pd.DataFrame(省份数据.get_group('湖北'))
# 为湖北省的数据添加累计确诊、累计治愈、累计死亡数据
添加累计确诊治愈死亡数据(湖北)
# 打印湖北省每月 15 日的疫情数据
print(湖北[湖北['日期'].dt.day == 15])

# 复制广东省的数据
广东 = pd.DataFrame(省份数据.get_group('广东'))
# 为广东省的数据添加累计确诊、累计治愈、累计死亡数据
添加累计确诊治愈死亡数据(广东)
# 打印广东省每月 15 日的疫情数据
广东[广东['日期'].dt.day == 15]


""" 任务三
简介：
根据任务1、2结果, 统计各省级行政单位每天新冠病人
的住院人数，输出湖北、广东每月 20 日的统计结果。

要求：
结果包含省份、日期、住院人数等数据。
"""


def 添加住院人数数据(城市数据: pd.DataFrame):
  """
  此函数通过引用传递修改原始数据, 请传入原始的 DataFrame
  或在传递参数时调用 DataFrame.copy() 方法。否则将会触发
  SettingWithCopyWarning 异常。
  """

  if '累计死亡' not in 城市数据.columns:
    添加累计确诊治愈死亡数据(城市数据)

  城市数据.sort_values(by='日期', inplace=True)
  城市数据['住院人数'] = 城市数据['累计确诊'] - (城市数据['累计治愈'] + 城市数据['累计死亡'])


# 为湖北省添加住院人数数据
添加住院人数数据(湖北)
# 打印湖北省每月 20 日的疫情数据
print(湖北[湖北['日期'].dt.day == 20])

# 为广东省添加住院人数数据
添加住院人数数据(广东)
# 打印广东省每月 20 日的疫情数据
广东[广东['日期'].dt.day == 20]


from typing import Callable
from pandas.core.groupby.generic import DataFrameGroupBy
import matplotlib.pyplot as 绘图
import numpy as np

""" 任务四
简介：
以可视化图表形式展示国内新冠疫情汇总概要信息、时空变化情况、重点关注区域等。
"""


# 字体设置
绘图.rcParams['font.family'] = 'microsoft yahei'
# 画布设置
绘图.figure(figsize=(20, 12), dpi=100)
# 画布子图位置设置
绘图.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
# 画布大标题
绘图.suptitle('各省新馆疫情确诊人数')


def 绘制各省新冠疫情确诊人数概要图(省份数据: DataFrameGroupBy):
  # 各省确诊数量表
  数据 = pd.DataFrame(columns=['省份名', '确诊数量'])
  # 统计各省确诊数量
  for 省份名 in 城市省份对照表['省份']:
    省份数据_副本 = pd.DataFrame(省份数据.get_group(省份名))
    省份总确诊数量 = 省份数据_副本['新增确诊'].sum()
    数据.loc[len(数据)] = [省份名, 省份总确诊数量]
  # 由大到小排序
  数据.sort_values(by='确诊数量', ascending=False, inplace=True)

  # 绘制柱状图
  绘图.subplot(3, 1, 1)
  绘图.title('各省新冠疫情确诊人数概要')
  绘图.bar(x=数据['省份名'], height=数据['确诊数量'])


def 绘制疫情趋势折线图(数据: pd.DataFrame, 数据筛选器: Callable[[pd.DataFrame], pd.DataFrame] | None, 图表标题: str, 图表位置: tuple[int, int, int], X轴文字旋转角度: int = 0):
  # 复制 '日期', '新增确诊', '新增治愈', '新增死亡' 列
  数据 = 数据[['日期', '新增确诊', '新增治愈', '新增死亡']].copy()
  添加累计确诊治愈死亡数据(数据)
  # 删除日期重复的行
  数据.drop_duplicates(subset='日期', keep='last', inplace=True)
  数据 = 补全缺失的日期数据(数据, 缺省列=['累计确诊', '累计治愈', '累计死亡'])
  # 过滤数据
  if 数据筛选器 is not None:
    数据 = 数据筛选器(数据)

  # 绘图
  绘图.subplot(图表位置[0], 图表位置[1], 图表位置[2])
  绘图.title(图表标题)
  绘图.plot(数据['index'], 数据['累计确诊'], label='累计确诊人数', color='blue')
  绘图.plot(数据['index'], 数据['累计治愈'], label='累计治愈人数', color='green')
  绘图.plot(数据['index'], 数据['累计死亡'], label='累计死亡人数', color='red')
  # 将 x 轴文字左旋 45 度防止重叠
  绘图.xticks(rotation=X轴文字旋转角度)
  # 显示图例
  绘图.legend()


def 绘制疫治疗情况概要饼图(数据: pd.DataFrame, 数据筛选器: Callable[[pd.DataFrame], pd.DataFrame] | None, 图表标题: str, 图表位置: tuple[int, int, int]):
  # 复制 '日期', '新增确诊', '新增治愈', '新增死亡' 列
  数据 = 数据[['日期', '新增确诊', '新增治愈', '新增死亡']].copy()
  添加累计确诊治愈死亡数据(数据)
  添加住院人数数据(数据)
  # 取按日期并累加后的
  数据 = 数据.iloc[len(数据) - 1]
  # 只保留 '日期', '住院人数', '累计治愈', '累计死亡' 列
  数据 = 数据[['住院人数', '累计治愈', '累计死亡']]

  if 数据筛选器 is not None:
    数据 = 数据筛选器(数据)

  绘图.subplot(图表位置[0], 图表位置[1], 图表位置[2])
  绘图.title(图表标题)
  绘图.pie(
    数据.values,
    labels=数据.index,
    autopct="%.2f%%",
    colors=['darkseagreen', 'cornflowerblue', 'coral'],
    explode=np.full(len(数据), 0.05),
    wedgeprops={ 'width': 0.55 }
  )



绘制各省新冠疫情确诊人数概要图(省份数据)

# 全国疫情趋势图
绘制疫情趋势折线图(
  数据=全国数据,
  数据筛选器=lambda df : df[df['index'].dt.day == 15],
  图表标题='全国疫情趋势图',
  图表位置=(3, 3, 4)
)

# 湖北省疫情趋势图
绘制疫情趋势折线图(
  数据=省份数据.get_group('湖北'),
  数据筛选器=lambda df : df[df['index'].dt.day.isin([10, 25])],
  图表标题='湖北省疫情趋势图',
  图表位置=(3, 3, 5),
  X轴文字旋转角度=45
)

# 广东省疫情趋势图
绘制疫情趋势折线图(
  数据=省份数据.get_group('广东'),
  数据筛选器=lambda df : df[df['index'].dt.day.isin([10, 25])],
  图表标题='广东省疫情趋势图',
  图表位置=(3, 3, 6),
  X轴文字旋转角度=45
)

# 全国新冠疫情治疗情况概要
绘制疫治疗情况概要饼图(全国数据, None, '全国新冠疫情治疗情况概要', (3, 3, 7))

# 湖北省新冠疫情治疗情况概要
绘制疫治疗情况概要饼图(省份数据.get_group('湖北'), None, '湖北省新冠疫情治疗情况概要', (3, 3, 8))

# 广东省新冠疫情治疗情况概要
绘制疫治疗情况概要饼图(省份数据.get_group('广东'), None, '广东省新冠疫情治疗情况概要', (3, 3, 9))

绘图.show()
