"""
读取CSV文件

Version: 0.1
Author: 骆昊
Date: 2018-03-13
"""

import csv

def main():

    # filename = 'example.csv' # 无法打开文件!: example.csv
    filename = 'teacher.csv'

    try:
        with open(filename) as f:
            reader = csv.reader(f)
            data = list(reader)
    except FileNotFoundError:
        print('无法打开文件!:',filename)
    else:
        for item in data:
            print('%-30s%-20s%-10s' % (item[0],item[1],item[2]))

if __name__ == '__main__':
    main()
