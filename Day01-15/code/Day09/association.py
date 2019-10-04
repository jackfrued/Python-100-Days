"""
对象之间的关联关系

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""

from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def move_to(self, x, y):
        self._x = x
        self._y = y

    def move_by(self, dx, dy):
        self._x += dx
        self._y += dy

    def distance_to(self, other):
        dx = self._x - other._x
        dy = self._y - other._y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self._x), str(self._y))


class Line(object):

    def __init__(self, start=Point(0, 0), end=Point(0, 0)):
        self._start = start
        self._end = end

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        self._start = start

    @property
    def end(self):
        return self.end

    @end.setter
    def end(self, end):
        self._end = end

    @property
    def length(self):
        return self._start.distance_to(self._end)


if __name__ == '__main__':
    p1 = Point(3, 5)
    print(p1)
    p2 = Point(-2, -1.5)
    print(p2)
    line = Line(p1, p2)
    print(line.length)
    line.start.move_to(2, 1)
    line.end = Point(1, 2)
    print(line.length)
