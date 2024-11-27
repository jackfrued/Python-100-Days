"""
实现进程间的通信

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""
import multiprocessing
import os

def sub_task1(queue):
    print('子进程进程号:',os.getpid())
    counter = 0
    while counter < 10:
        queue.put('Pong')
        counter += 1

def sub_task2(queue):
    counter = 0
    while counter < 10:
        queue.put('Ping')
        counter += 1

def main():
    print('当前进程号:', os.getpid())
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=sub_task1, args=(queue,))
    p1.start()
    p1.join()

    p2 = multiprocessing.Process(target=sub_task2, args=(queue,))
    p2.start()
    p2.join()

    print('子任务已经完成.')
    for _ in range(20):
        print(queue.get(), end='')

if __name__ == '__main__':
    main()
