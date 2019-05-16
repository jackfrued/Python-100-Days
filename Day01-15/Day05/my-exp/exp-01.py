"""
Author: Tang
Date：2019-05-15

"""

for i in range(100,1000):
    high = i //100
    mid = i//10 % 10
    low = i % 10
    if i == (high**3+mid**3+low**3):
        print("{} 是水仙花数".format(i))