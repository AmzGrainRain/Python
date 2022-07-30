import json as JSON

# json字符串转字典
json1 = '[{"name": "lkh", "age": 18}, {"name": "wzw", "age": 20 }]'
d1 = JSON.loads(json1)
print(d1)

# 字典转json字符串
d2 = [
  {
    'name': 'lkh',
    'age': 18
  },
  {
    'name': 'wzw',
    'age': 20
  }
]
json2 = JSON.dumps(d2, indent = 2)
print(json2)

