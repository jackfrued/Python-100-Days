#!/usr/bin/python3
from datetime import datetime
import sys


def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def get_days(year, month):
    days = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
            [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]
    return days[is_leap(year)][month - 1]


def main():
    if len(sys.argv) > 1:
        month = int(sys.argv[1])
        year = int(sys.argv[2])
    else:
        current_date = datetime.now()
        year = current_date.year
        month = current_date.month
    year2 = year if month >= 3 else year - 1
    c = year2 // 100
    y = year2 % 100
    m = month if month >= 3 else month + 12
    w = y + y // 4 + c // 4 - 2 * c + 26 * (m + 1) // 10
    w %= 7
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    print(f'{months[month - 1]} {year}'.center(20))
    print('Su Mo Tu We Th Fr Sa')
    print(' ' * 3 * w, end='')
    total_days = get_days(year, month)
    for day in range(1, total_days + 1):
        print(f'{day}'.rjust(2), end=' ')
        w += 1
        if w == 7:
            print()
            w = 0
    print()


if __name__ == '__main__':
    main()
