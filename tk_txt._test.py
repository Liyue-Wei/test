from tkinter import *

win = Tk()
win.title("C语言中文网")
# win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
win.geometry('400x420')
# 创建一个文本控件
# width 一行可见的字符数；height 显示的行数
text = Text(win, width=50, height=30, undo=True, autoseparators=False)
# 适用 pack(fill=X) 可以设置文本域的填充模式。比如 X表示沿水平方向填充，Y表示沿垂直方向填充，BOTH表示沿水平、垂直方向填充
text.pack()
# INSERT 光标处插入；END 末尾处插入
text.insert(INSERT, 'C语言中文网，一个有温度的网站')
win.mainloop()