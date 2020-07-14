"""
输入一个正整数判断它是不是素数
用while loop完成
"""
a = int(input('int = '))
while True:
    for i in range(2, a):
        if a % i != 0:
            print(f'{a} is a prime') 
        else:
            print(f'{a} is not a prime')
            break