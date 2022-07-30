import os
import sys
sys.path.append(os.getcwd())

def home():
  os.system('cls')
  print('============================================================')
  print('1. 新增数据')
  print('2. 删除数据')
  print('3. 更新数据')
  print('4. 查询数据')
  print('5. 列出数据')
  print('0. 退出')
  print('============================================================')

def add():
  os.system('cls')
  newBook = {
    'name': '',
    'explain': '',
    'price': '',
    'lending': {
      'state': False,
      'info': '-',
      'startDate': '-',
      'endDate': '-'
    }
  }
  newBook.name = input('[必填] 书名：')
  newBook.explain = input('[必填] 简介: ')
  newBook.price = input('[必填] 售价: ')
  newBook.lending.state = input('[可选] 是否出借: ')
  newBook.lending.info = input('[可选] 出借备注: ')
  newBook.lending.info = input('[可选] 出借信息: ')

fs = {
  'home': home,
  'add': add
}

def switch(name):
  try:
    fs.get(name)()
  except:
    print('无效输入')
