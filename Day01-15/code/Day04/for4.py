"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""
from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
# end = int(num) - 1
print('end is %d' %end)
is_prime = True
for x in range(2, end + 1):
    print('for x is %d' %x)
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

#判断是否素数，只需要试除到其根号对应的数即可
def is_prime(input):
    '''
    判断是否素数的方法
    :param int:
    :return:
    '''
    if not isinstance(input, int):
        print('the input is not int!')
        raise Exception('the input is not int!')
    num = int(input)
    end = int(sqrt(input))
    is_prime = True
    for x in range(2, end + 1):
        print('for x is %d' % x)
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print('%d是素数' % num)
        return True
    else:
        print('%d不是素数' % num)
        return False

is_prime(1.4)