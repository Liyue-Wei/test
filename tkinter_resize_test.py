import tkinter as tk
 
window = tk.Tk()
window.title("窗口缩放")
 
#设置窗口大小，并将窗口放置在屏幕中央
width = 400
height = 400
g_screenwidth = window.winfo_screenwidth()
g_screenheight = window.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (g_screenwidth-width)/2, (g_screenheight-height)/2)
window.geometry(alignstr)
 
#设置窗口背景为白色
window.config(bg='white')
#设置窗口最小尺寸
window.minsize(width, height)
 
#采用frame上添加Text方式，可根据窗口进行像素级缩放
frame1 = tk.Frame(window, width=360, height=340)
frame1.pack_propagate(0)
frame1.place(x=20, y=10)
 
text1 = tk.Text(frame1)
text1.pack(fill="both", expand="yes") 
 
#Text内部支持复制，粘贴
menubar = tk.Menu(window, tearoff=False)
 
def cut(editor, event=None):
	editor.event_generate("<<Cut>>")
def copy(editor, event=None):
	editor.event_generate("<<Copy>>")
def paste(editor, event=None):
	editor.event_generate('<<Paste>>')
def rightKey(event, editor):
	menubar.delete(0, 'end')
	menubar.add_command(label='剪切',command=lambda:cut(editor))
	menubar.add_command(label='复制',command=lambda:copy(editor))
	menubar.add_command(label='粘贴',command=lambda:paste(editor))
	menubar.post(event.x_root,event.y_root)
 
#绑定右键复制粘贴功能
text1.bind('<Button-3>', lambda x: rightKey(x, text1))
 
#测试按键
def testFunc():
	text1.insert('end', "hello world\n")
	text1.see('end')
	text1.update()
 
button1 = tk.Button(window, text="测试按键", bd=1, height=1, width=7, command=testFunc)
button1.place(x=20, y=360)
 
save_width = width
save_height = height
 
#窗口尺寸调整处理函数
def WindowResize(event):
	global save_width
	global save_height
	
	new_width = window.winfo_width()
	new_height = window.winfo_height()
	
	if new_width == 1 and new_height == 1:
		return
	if save_width != new_width or save_height != new_height:
		frame1.config(width=new_width-40, height=new_height-60)
		button1.place(x=20, y=new_height-40)
	save_width = new_width
	save_height = new_height
 
#绑定窗口变动事件
window.bind('<Configure>', WindowResize)
 
window.mainloop()