"""
元组的定义和使用

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    # 定义元组
    t = ('骆昊', 38, True, '四川成都')
    print(t)
    # 获取元组中的元素
    print(t[0])
    print(t[1])
    print(t[2])
    print(t[3])
    # 遍历元组中的值
    for member in t:
        print(member)
    # 重新给元组赋值
    # t[0] = '王大锤'      # TypeError
    # 变量t重新引用了新的元组 原来的元组被垃圾回收
    t = ('王大锤', 20, True, '云南昆明')
    print(t)
    # 元组和列表的转换
    person = list(t)
    print(person)
    person[0] = '李小龙'
    person[1] = 25
    print(person)
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)
    print(fruits_tuple[1])


if __name__ == '__main__':
    main()