"""
字符串常用操作 - 实现字符串倒转的方法

Version: 0.1
Author: 骆昊
Date: 2018-03-19
"""

from io import StringIO


def reverse_str1(str):
    return str[::-1]


def reverse_str2(str):
    if len(str) <= 1:
        return str
    return reverse_str2(str[1:]) + str[0:1]


def reverse_str3(str):
    # StringIO对象是Python中的可变字符串
    # 不应该使用不变字符串做字符串连接操作 因为会产生很多无用字符串对象
    rstr = StringIO()
    str_len = len(str)
    for index in range(str_len - 1, -1, -1):
        rstr.write(str[index])
    return rstr.getvalue()


def reverse_str4(str):
    return ''.join(str[index] for index in range(len(str) - 1, -1, -1))


def reverse_str5(str):
    # 将字符串处理成列表
    str_list = list(str)
    str_len = len(str)
    # 使用zip函数将两个序列合并成一个产生元组的迭代器
    # 每次正好可以取到一前一后两个下标来实现元素的交换
    for i, j in zip(range(str_len // 2), range(str_len - 1, str_len // 2, -1)):
        str_list[i], str_list[j] = str_list[j], str_list[i]
    # 将列表元素连接成字符串
    return ''.join(str_list)


if __name__ == '__main__':
    str = 'I love Python'
    print(reverse_str1(str))
    print(str)
    print(reverse_str2(str))
    print(str)
    print(reverse_str3(str))
    print(str)
    print(reverse_str4(str))
    print(str)
    print(reverse_str5(str))
    print(str)
