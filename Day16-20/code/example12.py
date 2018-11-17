"""
协程 - 可以通过yield来调用其它协程，yield将执行权转让给其他协程
协程之间不是调用者与被调用者的关系，而是彼此对称平等的
"""


def num_generator(start, end):
    """指定起始值的整数生成器"""
    for num in range(start, end + 1):
        yield num


def square_mapper(numbers):
    """将数值映射为其平方的协程"""
    for num in numbers:
        yield num ** 2


def prime_filter(numbers):
    """从数值中过滤出素数的协程"""
    for num in numbers:
        flag = True
        for factor in range(2, int(num ** 0.5 + 1)):
            if num % factor == 0:
                flag = False
                break
        if flag:
            yield num


def main():
    tasks = []
    tasks.append(square_mapper(num_generator(1, 100)))
    tasks.append(prime_filter(num_generator(2, 100)))
    for _ in range(100):
        for task in tasks:
            print(f'切换到任务{task.__name__} => ', end='')
            try:
                print(task.__next__())
            except StopIteration as error:
                print(error)


if __name__ == '__main__':
    main()
