"""
水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、
自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number），水仙花数是指一个 3 位数，
它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。

Version: 0.1
Author: Ifan
Date: 2019-06-09
"""
import math

for i in range(1000):
    if len(str(i)) == 1:
        if i**3 == i:
            print(i)
    elif len(str(i)) == 2:
        if int(str(i)[0])**3 + int(str(i)[1])**3 == i:
            print(i)
    elif len(str(i)) == 3:
        if int(str(i)[0])**3 + int(str(i)[1])**3 + int(str(i)[2])**3 == i:
            print(i)
    else:
        print("There are not Narcissistic Number")
