import os

# 判断文件是否存在
if os.path.exists('data'):
  os.remove('data')
else:
  print('文件不存在')

# 删除文件夹
#os.rmdir("myfolder")