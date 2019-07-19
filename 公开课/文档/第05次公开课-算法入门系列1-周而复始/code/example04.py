from functools import lru_cache


@lru_cache()
def fib(num):
    if num in (1, 2):
        return 1
    return fib(num - 1) + fib(num - 2)


for num in range(1, 101):
    print(f'{num}: {fib(num)}')
