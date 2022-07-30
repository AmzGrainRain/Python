# x = 2
# def fun1():
#   # 函数内部的变量与外部完全隔离
#   x = 1
#   print(x)

# # 打印 1
# fun1()
# # 打印 2
# print(x)




















# y = 2
# def fun2():
#   # 函数内部修改全局变量需要使用 global 关键字声明变量名
#   global y
#   y = 9
#   print(y)

# # 打印 9
# fun1()
# # 打印 9
# print(y)



















# def fun3():
#   test = 1
#   def fun4():
#     print(test)
#   fun4()

# # 从函数内的一个函数访问局部变量
# fun3()