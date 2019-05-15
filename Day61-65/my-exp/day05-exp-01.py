"""

Author: Tang
Date: 20190-5-15
找出100~999的水仙花数


"""
for i in range(100,1000):
    high = i // 100
    mid = i // 10 % 10
    low = i % 10
    num = high**3+mid**3+low**3
    if i == num:
        print("{}是水仙花数".format(i))