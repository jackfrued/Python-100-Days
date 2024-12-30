"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

flag = 0
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            flag += 1
            print("方案：%d" % flag)
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
            print("攻击：{}只，母鸡：{}只，小鸡：{}只".format(x, y, z))
            print("攻击：{0}只，母鸡：{1}只，小鸡：{2}只".format(x, y, z))
            print("攻击：{x}只，母鸡：{y}只，小鸡：{z}只".format(x = x, y = y, z = z))

