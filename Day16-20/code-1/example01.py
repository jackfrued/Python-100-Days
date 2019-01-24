"""
实现查找功能的模块
"""


def seq_search(items, elem):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == elem:
            return index
    return -1


def bin_search(items, elem):
    """折半查找(二分查找)"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if elem < items[mid]:
            end = mid - 1
        elif elem > items[mid]:
            start = mid + 1
        else:
            return mid
    return -1
