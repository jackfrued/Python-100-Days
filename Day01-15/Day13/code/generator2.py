"""
生成器 - 使用yield关键字

Version: 0.1
Author: 骆昊
Date: 2018-03-21
"""


def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n += 1


for x in fib(20):
    print(x)
