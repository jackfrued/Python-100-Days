"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
Differ: "1" 不是完美数
Version: 0.2
Author: Griffin Chen
Date: 2021-6-23
"""
import math

for num in range(2, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if 1 < factor != num // factor:
                result += num // factor
    if result == num:
        print(num)