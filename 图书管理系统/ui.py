import tkinter

# 创建主窗口
rootWindow = tkinter.Tk()



rootWindow.title('图书管理系统')
rootWindow.geometry('800x500')
rootWindow['background'] = '#eeeeee'
rootWindow.resizable(0, 0)
rootWindow.attributes('-topmost', True)


# 开启主循环
rootWindow.mainloop()