#!/usr/bin/python3
# coding: utf-8
from random import randint


def main():
    answer = randint(1, 100)
    while True:
        number = int(input('请输入: '))
        if number < answer:
            print('大一点')
        elif number > answer:
            print('小一点')
        else:
            print('恭喜你猜对了!')
            break


if __name__ == '__main__':
    main()
