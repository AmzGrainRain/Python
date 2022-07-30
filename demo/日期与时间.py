# 导入内置模块
import datetime as DT

# 输出日期
print(DT.datetime.now())
# 创建日期对象
dataTime = DT.datetime(2022, 6, 27, 1, 30, 29)
# 输出创建好的日期对象（2022-06-27 01:30:29）
print(dataTime)
# 格式化输出日期 (https://www.w3school.com.cn/python/python_datetime.asp)
print(dataTime.strftime('%B'))