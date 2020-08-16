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
    b = 100     # 局部变量
    print(b)


foo3()
print(b)


def foo4():
    global b
    b = 200     # 全局变量
    print(b)


foo4()
print(b)
