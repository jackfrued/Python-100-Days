"""
模拟面试编程题
"""


def second_max(items: list, gt=lambda x, y: x > y):
    """从列表中找出第二大元素"""
    assert len(items) >= 2
    max1, max2 = (items[0], items[1]) \
        if gt(items[0], items[1]) else (items[1], items[0])
    for i in range(2, len(items)):
        if gt(max1, items[i]) and gt(items[i], max2):
            max2 = items[i]
        elif gt(items[i], max1):
            max1, max2 = items[i], max1
    return max2


def list_depth(items: list) -> int:
    """计算嵌套列表的嵌套深度"""
    if isinstance(items, list):
        max_depth = 1
        for item in items:
            max_depth = max(list_depth(item) + 1, max_depth)
        return max_depth
    return 0


def main():
    """主函数"""
    one_set = {1}
    pos, off = 1, 1
    while pos <= 100000000:
        pos += off
        one_set.add(pos)
        off += 1
    num, *poses = map(int, input().split())
    for pos in poses:
        print(1 if pos in one_set else 0, end=' ')
    # items1 = [38, 95, 27, 95, 88, 73, 61, 50]
    # print(second_max(items1))
    # items2 = [[1], [[[2]]],[[3]], 4, [[[[[5, [6]]]]]]]
    # print(list_depth(items1))
    # print(list_depth(items2))


if __name__ == '__main__':
    main()
