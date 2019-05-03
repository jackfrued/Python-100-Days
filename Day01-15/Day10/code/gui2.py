"""
使用tkinter创建GUI
- 使用画布绘图
- 处理鼠标事件

Version: 0.1
Author: 骆昊
Date: 2018-03-14
"""

import tkinter


def mouse_evt_handler(evt=None):
    row = round((evt.y - 20) / 40)
    col = round((evt.x - 20) / 40)
    pos_x = 40 * col
    pos_y = 40 * row
    canvas.create_oval(pos_x, pos_y, 40 + pos_x, 40 + pos_y, fill='black')


top = tkinter.Tk()
# 设置窗口尺寸
top.geometry('620x620')
# 设置窗口标题
top.title('五子棋')
# 设置窗口大小不可改变
top.resizable(False, False)
# 设置窗口置顶
top.wm_attributes('-topmost', 1)
canvas = tkinter.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
canvas.bind('<Button-1>', mouse_evt_handler)
canvas.create_rectangle(0, 0, 600, 600, fill='yellow', outline='white')
for index in range(15):
    canvas.create_line(20, 20 + 40 * index, 580, 20 + 40 * index, fill='black')
    canvas.create_line(20 + 40 * index, 20, 20 + 40 * index, 580, fill='black')
canvas.create_rectangle(15, 15, 585, 585, outline='black', width=4)
canvas.pack()
tkinter.mainloop()

# 请思考如何用面向对象的编程思想对上面的代码进行封装
