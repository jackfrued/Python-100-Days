"""

使用tkinter创建GUI
- 在窗口上制作动画

Version: 0.1
Author: 骆昊
Date: 2018-03-14

"""

import tkinter
import time


# 播放动画效果的函数
def play_animation():
    canvas.move(oval, 2, 2)
    canvas.update()
    top.after(50, play_animation)


x = 10
y = 10
top = tkinter.Tk()
top.geometry('600x600')
top.title('动画效果')
top.resizable(False, False)
top.wm_attributes('-topmost', 1)
canvas = tkinter.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, 600, 600, fill='gray')
oval = canvas.create_oval(10, 10, 60, 60, fill='red')
canvas.pack()
top.update()
play_animation()
tkinter.mainloop()

# 请思考如何让小球碰到屏幕的边界就弹回
# 请思考如何用面向对象的编程思想对上面的代码进行封装
