"""
使用多线程的情况 - 模拟多个下载任务

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

from random import randint
from time import time, sleep
import threading


class DownloadTask(threading.Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        print('剩余时间%d秒.' % time_to_download)
        sleep(time_to_download)
        print('%s下载完成!' % self._filename)


def main():
    start = time()
    # 将多个下载任务放到多个线程中执行
    # 通过自定义的线程类创建线程对象 线程启动后会回调执行run方法
    thread1 = DownloadTask('Python从入门到住院.pdf')
    thread1.start()
    thread2 = DownloadTask('Peking Hot.avi')
    thread2.start()
    thread1.join()
    thread2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))


if __name__ == '__main__':
    main()

# 请注意通过threading.Thread创建的线程默认是非守护线程
