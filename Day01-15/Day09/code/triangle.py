"""
实例方法和类方法的应用

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""

from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # 静态方法
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and c + a > b

    # 实例方法
    def perimeter(self):
        return self._a + self._b + self._c

    # 实例方法
    def area(self):
        p = self.perimeter() / 2
        return sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))


if __name__ == '__main__':
    # 用字符串的split方法将字符串拆分成一个列表
    # 再通过map函数对列表中的每个字符串进行映射处理成小数
    a, b, c = map(float, input('请输入三条边: ').split())
    # 先判断给定长度的三条边能否构成三角形
    # 如果能才创建三角形对象
    if Triangle.is_valid(a, b, c):
        tri = Triangle(a, b, c)
        print('周长:', tri.perimeter())
        print('面积:', tri.area())
        # 如果传入对象作为方法参数也可以通过类调用实例方法
        # print('周长:', Triangle.perimeter(tri))
        # print('面积:', Triangle.area(tri))
        # 看看下面的代码就知道其实二者本质上是一致的
        # print(type(tri.perimeter))
        # print(type(Triangle.perimeter))
    else:
        print('不能构成三角形.')
