import os
import modules.menu as menu

class main:
  def __init__(this, locate):
    this.running = True
    this.locate = locate
    os.system('@echo off')
    os.system('title 图书管理系统')

  def start(this):
    while this.running:
      menu.switch(this.locate)

      # 获取输入信息
      this.op = input('> ')

      # 更新位置信息
      if this.op == '1': this.locate = 'add'
      if this.op == '0': this.running = False

mainProcess = main('home')
mainProcess.start()
