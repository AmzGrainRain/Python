# open(file, mode)
# mode:
# "x" - 将创建一个文件，如果文件存在则返回错误
# "a" - 如果指定的文件不存在，将创建一个文件
# "w" - 如果指定的文件不存在，将创建一个文件

# 打开文件
rf = open('data')
# 打印文件内容
print(rf.read())
# 关闭文件
rf.close()
