# 身份信息
class Person:
  def __init__(this, args):
    this.name = args['name']
    this.age = args['age']
    this.sex = args['sex']

  # 打印身份信息
  def personInfo(this):
    print('姓名：' + this.name)
    print('性别：' + this.sex)
    print('年龄：' + str(this.age))

# 学生信息
class Student(Person):
  def __init__(this, args):
    # 继承父类所有内容
    super().__init__({
      'name': args['name'],
      'age': args['age'],
      'sex': args['sex']
    })
    # 扩展属性
    this.score = args['score']

  # 打印学生信息
  def studentInfo(this):
    print('姓名：' + this.name)
    print('性别：' + this.sex)
    print('年龄：' + str(this.age))
    print('分数：' + str(this.score))


# 对象
xm = Student({
  'name': '小明',
  'age': 16,
  'sex': '男',
  'score': {
    '语文': 80,
    '数学': 60,
    '英语': 90
  }
})
# 打印身份信息
xm.personInfo()
# 打印学生信息
xm.studentInfo()