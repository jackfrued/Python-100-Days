"""
查找 - 顺序查找和二分查找
算法：解决问题的方法（步骤）
评价一个算法的好坏主要有两个指标：渐近时间复杂度和渐近空间复杂度，通常一个算法很难做到时间复杂度和空间复杂度都很低（因为时间和空间是不可调和的矛盾）
表示渐近时间复杂度通常使用大O标记
O(c)：常量时间复杂度 - 哈希存储 / 布隆过滤器
O(log_2 n)：对数时间复杂度 - 折半查找
O(n)：线性时间复杂度 - 顺序查找
O(n * log_2 n)：- 对数线性时间复杂度 - 高级排序算法（归并排序、快速排序）
O(n ** 2)：平方时间复杂度 - 简单排序算法（冒泡排序、选择排序、插入排序）
O(n ** 3)：立方时间复杂度 - Floyd算法 / 矩阵乘法运算
也称为多项式时间复杂度
O(2 ** n)：几何级数时间复杂度 - 汉诺塔
O(3 ** n)：几何级数时间复杂度
也称为指数时间复杂度
O(n!)：阶乘时间复杂度 - 旅行经销商问题 - NP
"""
from math import log2, factorial
from matplotlib import pyplot

import numpy


def seq_search(items: list, elem) -> int:
    """顺序查找"""
    for index, item in enumerate(items):
        if elem == item:
            return index
    return -1


def bin_search(items, elem):
    """二分查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if elem > items[mid]:
            start = mid + 1
        elif elem < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


def main():
    """主函数（程序入口）"""
    num = 6
    styles = ['r-.', 'g-*', 'b-o', 'y-x', 'c-^', 'm-+', 'k-d']
    legends = ['对数', '线性', '线性对数', '平方', '立方', '几何级数', '阶乘']
    x_data = [x for x in range(1, num + 1)]
    y_data1 = [log2(y) for y in range(1, num + 1)]
    y_data2 = [y for y in range(1, num + 1)]
    y_data3 = [y * log2(y) for y in range(1, num + 1)]
    y_data4 = [y ** 2 for y in range(1, num + 1)]
    y_data5 = [y ** 3 for y in range(1, num + 1)]
    y_data6 = [3 ** y for y in range(1, num + 1)]
    y_data7 = [factorial(y) for y in range(1, num + 1)]
    y_datas = [y_data1, y_data2, y_data3, y_data4, y_data5, y_data6, y_data7]
    for index, y_data in enumerate(y_datas):
        pyplot.plot(x_data, y_data, styles[index])
    pyplot.legend(legends)
    pyplot.xticks(numpy.arange(1, 7, step=1))
    pyplot.yticks(numpy.arange(0, 751, step=50))
    pyplot.show()


if __name__ == '__main__':
    main()
