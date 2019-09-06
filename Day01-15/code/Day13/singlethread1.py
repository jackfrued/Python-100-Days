"""
不使用多线程的情况 - 模拟多个下载任务

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

from random import randint
from time import time, sleep


def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('下载完成! 耗费了%d秒' % time_to_download)


def main():
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
