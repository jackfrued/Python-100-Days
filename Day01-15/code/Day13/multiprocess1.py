"""
使用Process类创建多个进程

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

# 通过下面程序的执行结果可以证实 父进程在创建子进程时复制了进程及其数据结构
# 每个进程都有自己独立的内存空间 所以进程之间共享数据只能通过IPC的方式


from multiprocessing import Process, Queue, current_process
from time import sleep


def sub_task(content, counts):
    print(f'PID: {current_process().pid}')
    counter = 0
    while counter < counts:
        counter += 1
        print(f'{counter}: {content}')
        sleep(0.01)


def main():
    number = random.randrange(5, 10)
    Process(target=sub_task, args=('Ping', number)).start()
    Process(target=sub_task, args=('Pong', number)).start()


if __name__ == '__main__':
    main()
