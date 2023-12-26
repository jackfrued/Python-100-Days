# 经典递归求解问题:
# 1. 迷宫寻路
# 2. 汉诺塔(梵塔)
# 3. 骑士周游
# 4. 八皇后


def f(n: int, m=1) -> int:
    if n == 0 or n == 1:
        return m
    return f(n - 1, n * m)


def sum(n: int) -> int:
    if n == 1:
        return 1
    return n + sum(n - 1)


def steps(n: int, m={}) -> int:
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        try:
            return m[n]
        except:
            m[n] = steps(n - 1) + steps(n - 2) + steps(n - 3)
            return m[n]


def list_depth(items: list) -> int:
    max_depth = 1 if isinstance(items, list) else 0
    if max_depth:
        for item in items:
            if isinstance(item, list):
                max_depth = max(max_depth, list_depth(item) + 1)
    return max_depth



def main():
    mylist = [1, ['a', ['b', ['c']]],[100, [200, 300, [400, [500, [600, [700]]]]]]] 
    thylist = [[], [[[]]], [[], []]]
    print(list_depth(mylist))
    print(list_depth(thylist))


if __name__ == '__main__':
    main()
