name = '小明'
age = 16


msg1 = '我叫 {} 今年 {} 岁。'
# 我叫 小明 今年 16 岁。
print(msg1.format(name, age))


msg2 = '我叫 {1} 今年 {0} 岁。'
# 我叫 小明 今年 16 岁。
print(msg2.format(age, name))


msg3 = '我叫 {1} 今年 {0} 岁。切记，我叫 {1}。'
# 我叫 小明 今年 16 岁。切记，我叫 小明。
print(msg3.format(age, name))


msg4 = '我叫 {name} 今年 {age} 岁。'
# 我叫 小明 今年 16 岁。
print(msg4.format(name = '小明', age = '16'))