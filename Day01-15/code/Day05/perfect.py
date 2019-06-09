"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

Version: 0.1
Author: 骆昊
Date: 2018-03-02

引入第二种解决方案进行对比
Version: 0.2
Author: Ifan
Date: 2018-06-09
"""
import threading
import time
import math

def planA(strPlan):
    start = time.process_time()
    for num in range(1, 10000):
        sum = 0
        for factor in range(1, int(math.sqrt(num)) + 1):
            if num % factor == 0:
                sum += factor
                if factor > 1 and num / factor != factor:
                    sum += num / factor
        if sum == num:
            print(" " + strPlan + " " + str(num))
    end = time.process_time()
    print(strPlan + "执行时间:", (end - start), "秒")

def planB(strPlan):
    start = time.process_time()
    for num1 in range(1, 10000):
        sum1 = 0
        for i in range(1, int(num1/2)+2):
            if num1 % i == 0:
                sum1 += i
        if sum1 == num1:
            print(" " + strPlan + " " + str(num1))
    end = time.process_time()
    print(strPlan + "执行时间:", (end - start), "秒")

threads = []
threads.append(threading.Thread(target=planA,args=('planA',)))
threads.append(threading.Thread(target=planB,args=('planB',)))

# 通过多线程让两个方案同时运行，比较上面两种不同的解决方案的执行时间 意识到优化程序的重要性

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
