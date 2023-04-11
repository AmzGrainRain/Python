from requests import get
from pyquery import PyQuery
from time import time as timestamp
from utils import init_dirs, get_extname, download_file
from shutil import move as move_file

# 初始化缓存目录、数据目录
init_dirs()

# 百度搜素结果页面
req_url = 'http://www.baidu.com/s?ie=utf-8&wd=' + input('请输入搜索内容：')

# 自定义请求头
headers = {
    'Cookie': 'BIDUPSID=9B7889B3883C47D0F303BC741E6D5F63; PSTM=1675847493; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=9B7889B3883C47D06E80465B7DA535F9:SL=0:NR=10:FG=1; newlogin=1; BDUSS=kJLeC1iSnpFY3RZLWVpaVdUMmJWbHhtczhTNWRPcGJtLXJDZndOfmp3aG9iRTlrRVFBQUFBJCQAAAAAABAAAAEAAADzYuH60NzVxsDPy767-gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGjfJ2Ro3ydkQ; BDUSS_BFESS=kJLeC1iSnpFY3RZLWVpaVdUMmJWbHhtczhTNWRPcGJtLXJDZndOfmp3aG9iRTlrRVFBQUFBJCQAAAAAABAAAAEAAADzYuH60NzVxsDPy767-gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGjfJ2Ro3ydkQ; ab_sr=1.0.1_Y2Y0NmQ3NTEyN2FmODRjODg2NzQzNTllNTQ5NGRkYWU2ZTYyNGVmYTM5NTE1OTIxMWI5MzU0M2U0MGI2ZDRmN2E0NTI1NjRiMGNjNDEwN2EzZTMwZDUxNjFiNGVlZjFiYTQ4YzcyY2YyZGE3YTI5YzY5OGIwZDgxZmYzNGQ4NGU2YzQ2ZTYxZmQxZDJhYjk5Nzk2N2FiMzk1NTVjYzNlNg==; BA_HECTOR=04ak812ka1ag24aha0a1a0581i2j6911m; BAIDUID_BFESS=9B7889B3883C47D06E80465B7DA535F9:SL=0:NR=10:FG=1; ZFY=l2dyP5wjgx3QkN:AguWdxPpUL2vafYp:Ajh1JHH4TdyDU:C; delPer=0; BD_CK_SAM=1; PSINO=7; BD_HOME=1; COOKIE_SESSION=2361_0_6_6_7_4_1_0_6_4_0_0_2361_0_4_0_1680447779_0_1680447775|9#9284_25_1679248112|9; sug=3; sugstore=1; ORIGIN=0; bdime=0; H_PS_PSSID=38185_36549_38470_38440_38400_38468_38290_38261_37926_38383_26350_38393_38420_38281_37881; H_PS_645EC=2ed4z7wrFfbYeKfm7n13yJC1SXpI6Usp1PwTPDK2d4VnThoCTAkfC6HJIpE; BDSVRTM=0; BD_UPN=12314753',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51',
    'Host': 'www.baidu.com',
    'Referer': 'pass.baidu.com'
}

# 发送 get 请求
req_res = get(url=req_url, headers=headers)

# 处理资源路径
html = req_res.text.replace('src="//', 'src="https://')

# 存储为 html 文件
html_file = open(file='./index.html', mode='w+', encoding='utf-8')
html_file.write(html)
html_file.close()

# 以 jQuery 的方式解析 html
jq = PyQuery(html)

# 获取所有 img 标签
all_img_tag = jq('img')

counter = 1
err = 0
# 遍历 img 标签，获取 src 属性并下载图片
for el in all_img_tag:
    # 文件名
    file_name = str(timestamp())
    # 图片路径
    file_path = download_file(jq(el).attr('src'), file_name)
    # 图片扩展名
    file_extname = get_extname(file_path)
    # 未知扩展名则跳过这轮循环
    if not file_extname:
        err += 1
        continue
    # 移动文件（重命名）
    move_file(file_path, f'./images/{file_name}.{file_extname}')
    print(f'请稍后... [{counter}/{len(all_img_tag)}]')
    counter += 1

print(f'完成，成功 {len(all_img_tag) - err} 个，失败 {err} 个。')
