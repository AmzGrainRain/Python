# 通过迭代器迭代元组
# mytuple = iter(('a', 'b', 'c'))
# print(next(mytuple))
# print(next(mytuple))
# print(next(mytuple))
























# 通过迭代器迭代字符串
# mystr = iter('xyz')
# print(next(mystr))
# print(next(mystr))
# print(next(mystr))



























# 通过 for 循环迭代字符串
# mystr1 = 'hello'
# for x in mystr1:
#   print(x)























# 使用迭代器迭代一个自定义的类/对象
# class Num:
#   def __init__(this, start, step, section, direction):
#     if start == section[0]: print('警告：初始值与限定区间重叠，迭代器无法正常工作。')
#     # 起始值
#     this.num = start
#     # 步进
#     this.step = step
#     # 区间
#     this.section = section
#     # 迭代方向
#     this.direction = direction

#   def __iter__(this):
#     return this

#   def __next__(this):
#     # 迭代区间 [section[0], section[1]]
#     if (this.num <= this.section[0] or this.num >= this.section[1]):
#       raise StopIteration
#       return
#     # 方向判定
#     if this.direction: this.num += this.step
#     else: this.num -= this.step
#     return this.num
# customIter = iter(Num(0, 1, [-1, 3], True))
# print(next(customIter))
# print(next(customIter))
# print(next(customIter))
# print(next(customIter))


