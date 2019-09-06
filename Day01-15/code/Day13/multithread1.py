"""
使用多线程的情况 - 模拟多个下载任务

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

from random import randint
from time import time, sleep
import atexit
import _thread


def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    print('剩余时间%d秒.' % time_to_download)
    sleep(time_to_download)
    print('%s下载完成!' % filename)


def shutdown_hook(start):
    end = time()
    print('总共耗费了%.3f秒.' % (end - start))


def main():
    start = time()
    # 将多个下载任务放到多个线程中执行
    thread1 = _thread.start_new_thread(download_task, ('Python从入门到住院.pdf',))
    thread2 = _thread.start_new_thread(download_task, ('Peking Hot.avi',))
    # 注册关机钩子在程序执行结束前计算执行时间
    atexit.register(shutdown_hook, start)


if __name__ == '__main__':
    main()

# 执行这里的代码会引发致命错误(不要被这个词吓到) 因为主线程结束后下载线程再想执行就会出问题
# 需要说明一下 由于_thread模块属于比较底层的线程操作而且不支持守护线程的概念
# 在实际开发中会有诸多不便 因此我们推荐使用threading模块提供的高级操作进行多线程编程
