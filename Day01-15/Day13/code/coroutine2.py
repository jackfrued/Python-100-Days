"""
使用协程 - 查看协程的状态

Version: 0.1
Author: 骆昊
Date: 2018-03-21
"""

from time import sleep
from inspect import getgeneratorstate


def build_deliver_man(man_id):
    total = 0
    while True:
        total += 1
        print('%d号快递员准备接今天的第%d单.' % (man_id, total))
        pkg = yield
        print('%d号快递员收到编号为%s的包裹.' % (man_id, pkg))
        sleep(0.5)


def package_center(deliver_man, max_per_day):
    num = 1
    # 创建状态(GEN_CREATED) - 等待开始执行
    print(getgeneratorstate(deliver_man))
    deliver_man.send(None)
    # 挂起状态(GEN_SUSPENDED) - 在yield表达式处暂停
    print(getgeneratorstate(deliver_man))
    # next(deliver_man)
    while num <= max_per_day:
        package_id = 'PKG-%d' % num
        deliver_man.send(package_id)
        num += 1
    deliver_man.close()
    # 结束状态(GEN_CLOSED) - 执行完毕
    print(getgeneratorstate(deliver_man))
    print('今天的包裹派送完毕!')


dm = build_deliver_man(1)
package_center(dm, 10)
