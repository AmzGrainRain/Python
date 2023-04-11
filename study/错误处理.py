try:
  # 手动抛出 TypeErrpr
  raise TypeErrpr('自定义错误')
except:
  print('捕获到一个错误')
else:
  print('没有引发错误')
finally:
  print('处理完成')