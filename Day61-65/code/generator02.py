from time import sleep


def countdown(n):
    while n > 0:
        yield n
        n -= 1


def main():
    for num in countdown(5):
        print(f'Countdown: {num}')
        sleep(1)
    print('Countdown Over!')


if __name__ == '__main__':
    main()
