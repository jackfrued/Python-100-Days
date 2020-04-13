"""
异常机制 - 处理程序在运行时可能发生的状态

Version: 0.1
Author: 骆昊
Date: 2018-03-13
"""

import time
import sys

filename = input('请输入文件名: ')
try:
    with open(filename) as f:
        lines = f.readlines()
except FileNotFoundError as msg:
    print('无法打开文件:', filename)
    print(msg)
except UnicodeDecodeError as msg:
    print('非文本文件无法解码')
    sys.exit()
else:
    for line in lines:
        print(line.rstrip())
        time.sleep(0.5)
finally:
    # 此处最适合做善后工作
    print('不管发生什么我都会执行')
