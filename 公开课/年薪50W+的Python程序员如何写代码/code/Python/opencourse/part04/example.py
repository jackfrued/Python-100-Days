import cProfile


# @profile
def is_prime(num):
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True


class PrimeIter:

    def __init__(self, total):
        self.counter = 0
        self.current = 1
        self.total = total

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.total:
            self.current += 1
            while not is_prime(self.current):
                self.current += 1
            self.counter += 1
            return self.current
        raise StopIteration()


@profile
def eat_memory():
    items = []
    for _ in range(1000000):
        items.append(object())
    return items


def main():
    eat_memory()
    # list(PrimeIter(1000))
    # cProfile.run('list(PrimeIter(10000))')


if __name__ == '__main__':
    main()
