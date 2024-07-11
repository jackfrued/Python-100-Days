import time
from concurrent.futures import ThreadPoolExecutor
from threading import Condition, Thread

class Account(object):
    """银行账户"""

    def __init__(self):
        self.balance = 0.0
        self.condition = Condition()

    def deposit(self, money):
        with self.condition:
            new_balance = self.balance + money
            time.sleep(0.01)
            self.balance = new_balance
            self.condition.notify_all()  # 通知所有等待的线程
            print(f'Deposited {money}, new balance is {self.balance}')

    def withdraw(self, money):
        with self.condition:
            while self.balance < money:
                self.condition.wait()  # 等待通知
            new_balance = self.balance - money
            time.sleep(0.01)
            self.balance = new_balance
            print(f'Withdrew {money}, new balance is {self.balance}')


def main():
    """主函数"""
    account = Account()
    with ThreadPoolExecutor(max_workers=10) as pool:
        for _ in range(5):
            pool.submit(account.deposit, 1)
            pool.submit(account.withdraw, 1)
    time.sleep(2)  # 等待所有线程完成
    print(f'Final balance: {account.balance}')


if __name__ == '__main__':
    main()
