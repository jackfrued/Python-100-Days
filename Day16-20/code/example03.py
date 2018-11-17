"""
递归(recursion)
"""


def fac(num):
    """求阶乘"""
    if num in (0, 1):
        return 1
    return num * fac(num - 1)


# 动态规划 - 把求解问题的中间结果保存起来
# 这种算法适合求解有最优子结构的问题或子问题会重复求解的问题
def fib(num, temp={}):
    """计算斐波拉切数"""
    # 递归的两个要素
    # 收敛条件 - 什么时候结束递归
    if num in (1, 2):
        return 1
    # 递归公式 - 降低问题的求解难度
    try:
        return temp[num]
    except KeyError:
        temp[num] = fib(num - 1) + fib(num - 2)
        return temp[num]


def fib2(total):
    """斐波拉切数列生成器"""
    num1, num2 = 0, 1
    for _ in range(total):
        num1, num2 = num2, num1 + num2
        yield num1


def main():
    """主函数"""
    for num in fib2(120):
        print(num)


if __name__ == '__main__':
    main()
