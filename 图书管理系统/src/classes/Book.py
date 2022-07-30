import uuid
from datetime import datetime
import json

class Book:
  ''' 增 '''
  def newData(this, args):
    # 读取并解析图书数据
    file = open('../data/books.txt', 'w+')
    try:
      books = json.loads(file.read())
      # 追加新书籍
      books.append({
        'name': args['name'],
        'explain': args['explain'],
        'price': args['price'],
        'lending': {
          'info': '-',
          'state': False,
          'startDate': '-',
          'endDate': '-'
        },
        'borrowing': datetime.now(),
        'borrowingVolume': 0,
        'salesVolume': 0,
        'id': uuid.uuid5(uuid.NAMESPACE_OID, 'book')
      })
      # 保存变更
      file.write(json.dumps(books))
    except:
      raise IOError('新增数据失败')
    finally:
      file.close()

  ''' 删 '''
  def deleteData(this, uuid):
    # 读取并解析图书数据
    file = open('../data/books.txt', 'w+')
    try:
      books = json.loads(file.read())
      # 找到要删除的数据
      for index, book in books:
        if book.uuid != uuid: continue
        del books[index]
        break
      # 保存变更
      file.write(json.dumps(books))
    except:
      raise IOError('删除数据失败, uuid: %s' % uuid)
    finally:
      file.close()

  ''' 改 '''
  def updateData(this, args):
    # 读取并解析图书数据
    file = open('../data/books.txt', 'w+')
    # 记录的数据
    record = [0, {}]
    try:
      books = json.loads(file.read())
      # 找到要修改的数据
      for index, book in books:
        if book.uuid != uuid: continue
        record[0] = index
        record[1] = book
        break
      # 更新数据
      
      # 保存变更
      books[record[0]] = record[1]
      file.write(json.dumps(books))
    except:
      raise IOError('删除数据失败, uuid: %s' % uuid)
    finally:
      file.close()
