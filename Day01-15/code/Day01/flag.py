"""
用Python的turtle模块绘制国旗
"""
import turtle


def draw_rectangle(x, y, width, height):
    """绘制矩形"""
    turtle.goto(x, y)       # 默认原点在中心，将原点向右移动x个像素，向上移动y个像素
    turtle.pencolor('red')
    turtle.fillcolor('red') # 设置填充色
    turtle.begin_fill()     # 开始填充
    for i in range(2):      # 走两遍以下步骤，每遍画一半；也可以不写循环，直接写完整
        turtle.forward(width)
        turtle.left(90)     # 乌龟面向右侧，left为上，right为下，数值表示转向角度
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()       #结束填充


def draw_star(x, y, radius):
    """绘制五角星"""
    turtle.setpos(x, y)
    pos1 = turtle.pos()
    turtle.circle(-radius, 72)
    pos2 = turtle.pos()
    turtle.circle(-radius, 72)
    pos3 = turtle.pos()
    turtle.circle(-radius, 72)
    pos4 = turtle.pos()
    turtle.circle(-radius, 72)
    pos5 = turtle.pos()
    turtle.color('yellow', 'yellow')
    turtle.begin_fill()
    turtle.goto(pos3)
    turtle.goto(pos1)
    turtle.goto(pos4)
    turtle.goto(pos2)
    turtle.goto(pos5)
    turtle.end_fill()


def main():
    """主程序"""
    turtle.speed(12)
    turtle.penup()
    x, y = -270, -180
    # 画国旗主体
    width, height = 540, 360
    draw_rectangle(x, y, width, height)
    # 画大星星
    pice = 22
    center_x, center_y = x + 5 * pice, y + height - pice * 5
    turtle.goto(center_x, center_y)
    turtle.left(90)
    turtle.forward(pice * 3)
    turtle.right(90)
    draw_star(turtle.xcor(), turtle.ycor(), pice * 3)
    x_poses, y_poses = [10, 12, 12, 10], [2, 4, 7, 9]
    # 画小星星
    for x_pos, y_pos in zip(x_poses, y_poses):
        turtle.goto(x + x_pos * pice, y + height - y_pos * pice)
        turtle.left(turtle.towards(center_x, center_y) - turtle.heading())
        turtle.forward(pice)
        turtle.right(90)
        draw_star(turtle.xcor(), turtle.ycor(), pice)
    # 隐藏海龟
    turtle.ht()
    # 显示绘图窗口
    turtle.mainloop()


if __name__ == '__main__':
    main()