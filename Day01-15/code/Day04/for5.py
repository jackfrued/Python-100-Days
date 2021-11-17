"""
输入两个正整数计算最大公约数和最小公倍数
"""
a = x = int(input('a = '))
b = y = int(input('b = '))

if a < b:
    a, b = b, a
c = a % b
while c != 0:
    a, b = b, c
    c = a % b
# for i in range(1, min(a,b) + 1):
#     if a % i == 0 and b % i == 0:
#         c = i
print(f'{b} is the gcd of {x} and {y}')


# for j in range(max(a,b), a * b + 1):
#     if j % a == 0 and j % b == 0:
#         d = j
d = x * y / b
print(f'{d} is the lcm of {x} and {y}')
