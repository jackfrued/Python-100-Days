
import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b < c or a + c < b or b + c < a:
    print('%.1f, %.1f, and %.1f can not be edges of a triangle' % (a, b, c))
else:
    p = a + b + c
    s = p / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print('The perimeter of this trangle is %.1f, and the area of it is %.1f' % (p, area) )