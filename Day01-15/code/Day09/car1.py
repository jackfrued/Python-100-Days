"""
属性的使用
- 访问器/修改器/删除器
- 使用__slots__对属性加以限制

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""


class Car(object):

    __slots__ = ('_brand', '_max_speed')

    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @brand.deleter
    def brand(self):
        del self._brand

    @property
    def max_speed(self):
        return self._max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError('Invalid max speed for car')
        self._max_speed = max_speed

    def __str__(self):
        return 'Car: [品牌=%s, 最高时速=%d]' % (self._brand, self._max_speed)


car = Car('QQ', 120)
print(car)
# ValueError
# car.max_speed = -100
car.max_speed = 320
car.brand = "Benz"
# 使用__slots__属性限制后下面的代码将产生异常
# car.current_speed = 80
print(car)
# 如果提供了删除器可以执行下面的代码
# del car.brand
# 属性的实现
print(Car.brand)
print(Car.brand.fget)
print(Car.brand.fset)
print(Car.brand.fdel)
# 通过上面的代码帮助学生理解之前提到的包装器的概念
# Python中有很多类似的语法糖后面还会出现这样的东西
