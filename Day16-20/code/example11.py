"""
自定义迭代器
"""


class Fibo:
    """斐波拉切数列迭代器"""

    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()


def main():
    """主函数"""
    for val in Fibo(10):
        print(val)
    print('-' * 10)
    fibo_iter = Fibo(10)
    for _ in range(10):
        print(next(fibo_iter))


if __name__ == '__main__':
    main()
