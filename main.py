#coding:utf-8
from Tkinter import *
from function import *

root = Tk()
root.title("宇宙超级无敌屌炸天的笔记本")
root.geometry("500x500+100+100")

#创建菜单栏
menubar = Menu(root)  
root.config(menu=menubar)

filemenu = Menu(menubar)
filemenu.add_command(label='新建',accelerator='Ctrl + N',command=new)
filemenu.add_command(label='打开',accelerator='Ctrl + O',command=open)
filemenu.add_command(label='保存',accelerator='Ctrl + S',command=save)
filemenu.add_command(label='另存为',accelerator='Ctrl + Shift + S',command=saveas)
menubar.add_cascade(label='文件',menu=filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label='撤销',accelerator='Ctrl + Z')
editmenu.add_command(label='重做',accelerator='Ctrl + Y')
editmenu.add_separator()
editmenu.add_command(label='剪切',accelerator='Ctrl + X')
editmenu.add_command(label='复制',accelerator='Ctrl + C')
editmenu.add_command(label='粘贴',accelerator='Ctrl + V')
editmenu.add_separator()
editmenu.add_command(label='查找',accelerator='Ctrl + F')
editmenu.add_command(label='全选',accelerator='Ctrl + A')
menubar.add_cascade(label='编辑',menu=editmenu)

aboutmenu = Menu(menubar)
aboutmenu.add_command(label='作者')
aboutmenu.add_command(label='版权')
menubar.add_cascade(label='关于',menu=aboutmenu)
root.mainloop()
