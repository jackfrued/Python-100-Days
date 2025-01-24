"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

print("100~999之间的所有水仙花数有：", end=' ')
for num in range(100, 1000):
    low = num % 10          # 个位数
    mid = num // 10 % 10    # 十位数
    high = num // 100       # 百位数

    if num == low ** 3 + mid ** 3 + high ** 3:
        print("%d" %num, end=' ')
