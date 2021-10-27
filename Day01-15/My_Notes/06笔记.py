# 文档中的例题

# 例题1：函数的作用
"""
输入M和N计算C(M,N)

Version: 0.1
Author: 骆昊
"""
def fac(num):
    """求阶乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


m = int(input('m = '))
n = int(input('n = '))
# 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
print(fac(m) // fac(n) // fac(m - n))
# 【疑问】为啥这里要用双斜杠取整呢？

'''
说明： Python的math模块中其实已经有一个名为factorial函数实现了阶乘运算，
事实上求阶乘并不用自己定义函数。下面的例子中，我们讲的函数在Python标准库已经实现过了，
我们这里是为了讲解函数的定义和使用才把它们又实现了一遍，
实际开发中并不建议做这种低级的重复劳动。
'''
# 你觉得上面最后这句话很TM认同


# 例题2：函数的重载
from random import randint


def roll_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c


# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))

# 这个方便啊，还能只给部分参数设定值，
# 这和MATLAB函数有点像


# 练习（这次只是学习，下次复写一遍！）

# 练习1：实现计算求最大公约数和最小公倍数的函数。
def gcd(x,y):
    """求最大公约数"""

# 标准答案：内含新的格式操作
def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y) 
    # 【新写法】上面的
    for factor in range(x, 0, -1): # 【新写法】
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)

# 练习2：实现判断一个数是不是回文数的函数。

# 标准答案：这个是函数基础课经典案例
def is_palindrome(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

# 练习3：实现判断一个数是不是素数的函数。

# 标准答案：求平方根还可以用指数运算：
def is_prime(num):
    """判断一个数是不是素数"""
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False

# 练习4：写一个程序判断输入的正整数是不是回文素数

# 标准答案：
if __name__ == '__main__':
    num = int(input('请输入正整数: '))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)
'''
当我们**将代码中重复出现的和相对独立的功能抽取成函数**后，
我们可以**组合使用这些函数**来解决更为复杂的问题，
这也是我们为什么要定义和使用函数的一个非常重要的原因。
'''




