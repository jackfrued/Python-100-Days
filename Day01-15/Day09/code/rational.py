"""
运算符重载 - 自定义分数类

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""

from math import gcd


class Rational(object):

    def __init__(self, num, den=1):
        if den == 0:
            raise ValueError('分母不能为0')
        self._num = num
        self._den = den
        self.normalize()

    def simplify(self):
        x = abs(self._num)
        y = abs(self._den)
        factor = gcd(x, y)
        if factor > 1:
            self._num //= factor
            self._den //= factor
        return self

    def normalize(self):
        if self._den < 0:
            self._den = -self._den
            self._num = -self._num
        return self

    def __add__(self, other):
        new_num = self._num * other._den + other._num * self._den
        new_den = self._den * other._den
        return Rational(new_num, new_den).simplify().normalize()

    def __sub__(self, other):
        new_num = self._num * other._den - other._num * self._den
        new_den = self._den * other._den
        return Rational(new_num, new_den).simplify().normalize()

    def __mul__(self, other):
        new_num = self._num * other._num
        new_den = self._den * other._den
        return Rational(new_num, new_den).simplify().normalize()

    def __truediv__(self, other):
        new_num = self._num * other._den
        new_den = self._den * other._num
        return Rational(new_num, new_den).simplify().normalize()

    def __str__(self):
        if self._num == 0:
            return '0'
        elif self._den == 1:
            return str(self._num)
        else:
            return '(%d/%d)' % (self._num, self._den)


if __name__ == '__main__':
    r1 = Rational(2, 3)
    print(r1)
    r2 = Rational(6, -8)
    print(r2)
    print(r2.simplify())
    print('%s + %s = %s' % (r1, r2, r1 + r2))
    print('%s - %s = %s' % (r1, r2, r1 - r2))
    print('%s * %s = %s' % (r1, r2, r1 * r2))
    print('%s / %s = %s' % (r1, r2, r1 / r2))
