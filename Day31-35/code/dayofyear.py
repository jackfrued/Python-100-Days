import sys
import mycal


def main():
    if len(sys.argv) != 4:
        print('Not enough arguments')
        return 
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    day = int(sys.argv[3])
    total = 0
    for m in range(1, month):
        total += mycal.get_days(year, m)
    total += day
    print(f'{year}年{month}月{day}日是{year}年的第{total}天')


if __name__ == '__main__':
    main()

