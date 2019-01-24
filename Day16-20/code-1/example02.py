"""
排序 - 冒泡排序(简单O(N**2)) / 归并排序(高级O(N*log2N))
冒泡排序
34, 99, 52, 11, 47, 68, 50, 84
34, 52, 11, 47, 68, 50, 84, 99
34, 11, 47, 52, 50, 68, 84
11, 34, 47, 50, 52, 68

快速排序
34, 99, 52, 11, 47, 68, 50, 84
{34, 11, 47}, {50}, {99, 52, 68, 84}
{11}, {34}, {47}, {50}, {52, 68, 84}, {99}
{11}, {34}, {47}, {50}, {52}, {68, 84}, {99}
{11}, {34}, {47}, {50}, {52}, {68}, {84}, {99}

归并排序 - 分治法(divide-and-conquer)
34, 99, 52, 11, 47, 68, 50, 84
{34, 99, 52, 11}, {47, 68, 50, 84}
{34, 99}, {52, 11}, {47, 68}, {50, 84}
{34}, {99}, {52}, {11}, {47}, {68}, {50}, {84}
{34, 99}, {11, 52}, {47, 68}, {50, 84}
{11, 34, 52, 99}, {47, 50, 68, 84}
{11, 34, 47, 50, 52, 68, 84, 99}

在使用分治法的时候通常都会使用到递归调用这种编程手段
一个函数直接或间接的调用了自身就称之为递归调用
"""


# 9 1 2 3 4 5 6 7 8
# 2 3 4 5 6 7 8 9 1
# *前面的参数称为位置参数, *后面的参数称为命名关键字参数
# 所谓命名关键字参数就是调用函数时必须以"参数名=参数值"的形式传入参数
def bubble_sort(origin_items, *, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = origin_items[:]
    length = len(items)
    for i in range(1, length):
        swapped = False
        for j in range(0, length - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(length - i - 1, i - 1, -1):
                if comp(items[j - 1], items[j]):
                    items[j - 1], items[j] = items[j], items[j - 1]
                    swapped = True
        if not swapped:
            break
    return items


def merge(list1, list2, comp=lambda x, y: x <= y):
    """"有序合并(将两个有序的列表合并成一个新的有序的列表)"""
    list3 = []
    index1, index2 = 0, 0
    while index1 < len(list1) and index2 < len(list2):
        if comp(list1[index1], list2[index2]):
            list3.append(list1[index1])
            index1 += 1
        else:
            list3.append(list2[index2])
            index2 += 1
    list3 += list1[index1:]
    list3 += list2[index2:]
    return list3


def merge_sort(origin_items, comp=lambda x, y: x <= y):
    """归并排序"""
    if len(origin_items) <= 1:
        return origin_items[:]
    mid = len(origin_items) // 2
    left = merge_sort(origin_items[:mid], comp)
    right = merge_sort(origin_items[mid:], comp)
    return merge(left, right, comp)


class Person:
    """人"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name}: {self.age}'


def main():
    # list1 = [12, 35, 48, 87, 92]
    # list2 = [39, 44, 50, 60, 77, 88]
    # list3 = merge(list1, list2)
    # print(list3)
    items = [34, 99, 52, 11, 47, 50, 84]
    print(items)
    print(merge_sort(items))
    # items = ['hi', 'hello', 'orange', 'watermelon', 'zoo', 'pitaya']
    # items = [
    #     Person("LuoHao", 38), Person("Baiyuanfang", 25),
    #     Person("Zhangsanfeng", 120), Person("Lee", 18)
    # ]
    # new_items = bubble_sort(items, comp=lambda x, y: len(x) > len(y))
    # new_items = bubble_sort(items, comp=lambda x, y: x.age > y.age)
    # print(items)
    # print(new_items)


if __name__ == '__main__':
    main()

