"""
作用域问题

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""


# 局部作用域
def foo1():
    a = 5


foo1()
# print(a)  # NameError

# 全局作用域
b = 10


def foo2():
    print(b)


foo2()


def foo3():
    print("foo3")
    b = 100     # 局部变量
    print(b)    # 函数内部是局部变量的地盘，局部变量与全局变量同名时可体现


foo3()
print(b)        # 函数外部是全局部变量的地盘，局部变量与全局变量同名时可体现


def foo4():
    global b    # 函数内部定义全局变量，会覆盖掉原来在之前其他位置定义的全局变量
    b = 200     # 全局变量
    print(b)


foo4()
print(b)
