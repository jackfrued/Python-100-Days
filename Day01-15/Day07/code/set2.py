"""
集合的常用操作
- 交集
- 并集
- 差集
- 子集
- 超集

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    set1 = set(range(1, 7))
    print(set1)
    set2 = set(range(2, 11, 2))
    print(set2)
    set3 = set(range(1, 5))
    print(set1 & set2)
    # print(set1.intersection(set2))
    print(set1 | set2)
    # print(set1.union(set2))
    print(set1 - set2)
    # print(set1.difference(set2))
    print(set1 ^ set2)
    # print(set1.symmetric_difference(set2))
    print(set2 <= set1)
    # print(set2.issubset(set1))
    print(set3 <= set1)
    # print(set3.issubset(set1))
    print(set1 >= set2)
    # print(set1.issuperset(set2))
    print(set1 >= set3)
    # print(set1.issuperset(set3))


if __name__ == '__main__':
    main()
