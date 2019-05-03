"""
多个线程共享数据 - 有锁的情况

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

import time
import threading


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = threading.Lock()

    def deposit(self, money):
        # 获得锁后代码才能继续执行
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            time.sleep(0.01)
            self._balance = new_balance
        finally:
            # 操作完成后一定要记着释放锁
            self._lock.release()

    @property
    def balance(self):
        return self._balance


if __name__ == '__main__':
    account = Account()
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        threading.Thread(target=account.deposit, args=(1,)).start()
    # 等所有存款的线程都执行完毕
    time.sleep(2)
    print('账户余额为: ￥%d元' % account.balance)

# 想一想结果为什么不是我们期望的100元
