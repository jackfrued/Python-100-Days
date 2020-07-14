"""
输入两个正整数计算最大公约数和最小公倍数
"""
a = int(input('a = '))
b = int(input('b = '))

for i in range(1, min(a,b) + 1):
    if a % i == 0 and b % i == 0:
        c = i
print(f'{c} is the gcd of {a} and {b}')


# for j in range(max(a,b), a * b + 1):
#     if j % a == 0 and j % b == 0:
#         d = j
d = a * b / c
print(f'{d} is the lcm of {a} and {b}')
