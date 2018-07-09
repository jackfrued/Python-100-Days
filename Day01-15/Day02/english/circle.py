"""

Enter the radius to calculate the perimeter and area of the circle

Version: 0.1
Author: 骆昊
Date: 2018-02-27

"""

import math

radius = float(input('Enter the radius : '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('Perimeter: %.2f' % perimeter)
print('Area: %.2f' % area)
