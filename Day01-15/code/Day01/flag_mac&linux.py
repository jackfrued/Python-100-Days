# coding:utf-8
# 5号国旗
import turtle
import math

turtle.setup(0.8, 0.8, 0, 0)  # 弹出框初始比例和海龟初始位置
turtle.speed(100)  # 绘图速度

def moveWithoutPaint(x, y):
    turtle.goto(x, y)
    turtle.up()

# 画长方形函数
def drawRectangle(color, x, y, angle):
    turtle.color(color, color)  # 设置画笔颜色和填充颜色
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(x)  # 画直线
        turtle.left(angle)  # left是当前方向水平往左开始旋转，当前线向上垂直的时候为left90
        turtle.forward(y)
        turtle.left(angle)
    turtle.end_fill()

# 等比例找到实际坐标，实际为圆底的坐标，所以要下移动半径，这个是为了测试验证五角星是否正确，找到圆底坐标，可剔除。
def newCenterList(centerList, stepLength, x0, y0,R):
    newlist = []
    for i in centerList:
        newlist.append([x0 + i[0] * stepLength,y0 + (-2 * y0 / 2) + i[1] * stepLength -R])
    return newlist

#原点的位置
def CenterList(centerList, stepLength, x0, y0):
    newlist = []
    for i in centerList:
        newlist.append([x0 + i[0] * stepLength,y0 + (-2 * y0 / 2) + i[1] * stepLength])
    return newlist

# 画圆形：因为turtle的圆是从底部开始的，所以坐标要往下移动一个半径，这个为了测试方便，可以不调用。
def drawCircle(CenterList, R, color):
    for i in CenterList:
        moveWithoutPaint(i[0], i[1])
        turtle.color(color, color)  # 设置画笔颜色和填充颜色
        turtle.begin_fill()
        turtle.circle(R)
        turtle.end_fill()
    turtle.up()

#重置五角星的方向
def returnStarReset(str):
    if str=="B":
        turtle.right(108)
    elif str=="S":
        turtle.right(18)

'''
画星星：由于forward会保留之前一个forward的方向，所以要在画星星前调整方向。
大星星是从水平正东的方向开始画的；而小星星是从上一个小星星的方向开始画的。所以角度不同
'''
def drawStar(color, r,str):
    turtle.color(color, color)
    turtle.begin_fill()
    returnStarReset(str)
    for _ in range(5):
        turtle.forward(r)
        turtle.left(144)
    turtle.left(-144)
    turtle.end_fill()
    turtle.up()

def drawStar4Mac(color, r,str):
    turtle.color(color, color)
    turtle.begin_fill()
    returnStarReset(str)
    for _ in range(5):
        turtle.forward(r)
        turtle.right(72)
        turtle.forward(r)
        turtle.left(144)
    turtle.left(-144)
    turtle.end_fill()
    turtle.up()

#计算小星星离大星星的角度以及到交接圆的顶点距离
def countTan(BPoint,SPoint,R):
    print(math.degrees(math.atan(1)))
    bX=BPoint[0][0]
    bY=BPoint[0][1]
    newlist=[]
    for i in SPoint:
        tmpx=float(i[0] - bX)
        tmpy=float(i[1] - bY)
        pointT= (tmpy/tmpx) #j计算tan值
        pointAT=math.degrees(math.atan(pointT))#反计算角度值，并且返回成与正东方向的夹角弧度
        pointHypotenuse=math.sqrt(math.pow(tmpx,2)+math.pow(tmpy,2))-R#要减去圆的半径才是交点。
        newlist.append([pointAT,pointHypotenuse])
    return newlist

length = 960  # 长
width = 640  # 宽
x0 = -length / 2  # 起始的坐标原点x
y0 = -width / 2  # 起始的坐标原点y
bigStarR = length / 2 / 15 * 3  # 大星星的半径
smallStarR = length / 2 / 15  # 小星星的半径
stepLength = length / 2 / 15  # 等分步长，经过计算，x 轴与y 轴是一样的步长因为960/2/15=640/2/10，长宽比是1.5:1
oringinalBPoint = [[5, 5]]  # 大圆心坐标
oringinalSPoint = [[10, 8], [12, 6], [12, 3], [10, 1]]  # 小圆心坐标
#圆的测试
bigCenterList = newCenterList(oringinalBPoint, stepLength, x0, y0, bigStarR)  # 比例放大之后的大星星圆底坐标
smallCenterList = newCenterList(oringinalSPoint , stepLength, x0, y0, smallStarR)  # 比例放大之后的大星星圆心坐标
#实际圆心坐标
BPoint = CenterList(oringinalBPoint, stepLength, x0, y0) # 比例放大之后的大星星圆心坐标
SPoint = CenterList(oringinalSPoint, stepLength, x0, y0) # 比例放大之后的小星星圆心坐标
sinValue=float(abs(math.sin(math.radians(72))))#因为sin函数里面是弧度，所以要先将72度角度，可用radians函数，其实也就是0.4pi。
bigStarLength = 2 * bigStarR * sinValue #python的编译会逐个替换，再算sin，会导致turtle的方便改变
smallStarLength = 2 * smallStarR * sinValue

#考虑到mac下的填充和windows的填充不一样，因此画五角星的函数也不一样。
bigStarLength4Mac=bigStarLength/(2+2*math.sin(math.radians(18)))
smallStarLength4Mac=smallStarLength/(2+2*math.sin(math.radians(18)))

# 初始化原点位置
moveWithoutPaint(x0, y0)

# 画红旗背景
drawRectangle("red", length, width, 90)

#用以核对星星的位置是否正确，是否在圆心的连接线上
#drawCircle(bigCenterList, bigStarR, "blue")
#drawCircle(smallCenterList, smallStarR, "blue")

#画完红旗之后找到大星星的顶点位置
moveWithoutPaint(BPoint[0][0], BPoint[0][1]+bigStarR )
#drawStar("yellow", bigStarLength,"B")
drawStar4Mac("yellow", bigStarLength4Mac,"B")
turtle.goto(BPoint[0][0], BPoint[0][1])#回到顶点位置
turtle.right(108)#回到正东方向，根据格子之间的tan值计算角度

#计算要旋转的角度以及要移动的方向，再画五角星。
smallStarP=countTan(BPoint,SPoint,smallStarR)

for i in smallStarP:
    turtle.left(i[0])
    turtle.forward(i[1])
    #drawStar("yellow", smallStarLength, "S")
    drawStar4Mac("yellow", smallStarLength4Mac, "S")
    turtle.left(162)
    turtle.left(-i[0])#记得还原回到正东方向
    turtle.goto(BPoint[0][0], BPoint[0][1])

turtle.hideturtle()
turtle.mainloop()