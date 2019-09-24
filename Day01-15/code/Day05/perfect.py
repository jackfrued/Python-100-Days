"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
for num in range(1, 10000):
    result = 0
    for factor in range(1, num):
        if num % factor == 0:
            result += factor
    if num == result:
        print(num)
