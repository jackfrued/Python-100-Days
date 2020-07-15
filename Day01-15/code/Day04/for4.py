"""
输入一个正整数判断它是不是素数
用while loop完成
"""
a = int(input('int = '))
if a == 1:
    print(f'{a} is not a prime')
else:
    i = 2
    while i < a:
        if a % i == 0:
            print(f'{a} is not a prime') 
            break
        i += 1
    else:
        print(f'{a} is a prime')