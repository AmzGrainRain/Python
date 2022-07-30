from time import time
import random

def uid():
  tmp1 = str(int(time()))
  tmp2 = []
  for x in tmp1:
    tmp2.append(x)
  random.shuffle(tmp2)
  tmp1 = ''
  for x in tmp2:
    tmp1 += x
  
  return tmp1

print(uid())