#!/usr/bin/python3
from datetime import datetime

import sys


def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def main():
    if len(sys.argv) == 3:
        month = int(sys.argv[1])
        year = int(sys.argv[2])
    else:
        now = datetime.now()
        date = now.date
        month = now.month
        year = now.year
    m, y = (month, year) if month >= 3 else (month + 12, year - 1)
    c, y = y // 100, y % 100
    w = (y + y // 4 + c // 4 - 2 * c + 26 * (m + 1) // 10) % 7
    month_words = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    print(f'{month_words[month - 1]} {year}'.center(20))
    print('Su Mo Tu We Th Fr Sa')
    print(' ' * 3 * w, end='')
    days = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap(year)][month - 1]   
    for day in range(1, days + 1):
        print(str(day).rjust(2), end=' ')
        w += 1
        if w == 7:
            print()
            w = 0
    print()

def get_days(year, month):
    """
    获取指定年份和月份的天数
    """
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        if is_leap(year):
            return 29
        else:
            return 28
    else:
        return None  # 对于非法的月份返回 None

if __name__ == '__main__':
    main()
