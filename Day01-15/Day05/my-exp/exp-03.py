"""
Author: Tang

Date: 2019-05-16

"""


for x in range(0,21):
    for y in range(0,34):
        if 14*x+8*y == 200:
            print("公鸡 {} 只, 母鸡 {} 只, 小鸡 {} 只".format(x,y,100-x-y))