import time


def get_narcissistic_number():
    '''
    寻找水仙花数，返回所有的水仙花数列表
    :return:
    '''
    start = time.time()
    print(start)
    narci_list = []
    for num in range(100, 1000):
        hundreds = num // 100
        tens = num // 10 % 10
        units = num % 10
        print('the %d is divide into %d %d %d' % (num, hundreds, tens, units))
        if hundreds ** 3 + tens ** 3 + units **3 == num:
            narci_list.append(num)
    print(narci_list)
    end = time.time()
    print(end)
    print('use time is %f second' % (end - start))
    return narci_list

def get_perfect_num():
    '''
    获得完美数
    :return:
    '''

if __name__ == '__main__':
    get_narcissistic_number()