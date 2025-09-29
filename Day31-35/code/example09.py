"""
装饰器 - 装饰器中放置的通常都是横切关注（cross-concern）功能
所谓横切关注功能就是很多地方都会用到但跟正常业务又逻辑没有必然联系的功能
装饰器实际上是实现了设计模式中的代理模式 - AOP（面向切面编程）
"""
from functools import wraps
from random import randint
from time import time, sleep

import pymysql


def record(output):

    def decorate(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            ret_value = func(*args, **kwargs)
            output(func.__name__, time() - start)
            return ret_value

        return wrapper

    return decorate


def output_to_console(fname, duration):
    print('%s: %.3f秒' % (fname, duration))


def output_to_file(fname, duration):
    with open('log.txt', 'a') as file_stream:
        file_stream.write('%s: %.3f秒\n' % (fname, duration))


def output_to_db(fname, duration):
    con = pymysql.connect(host='localhost', port=3306,
                          database='test', charset='utf8',
                          user='root', password='123456',
                          autocommit=True)
    try:
        with con.cursor() as cursor:
            cursor.execute('insert into tb_record values (default, %s, %s)',
                           (fname, '%.3f' % duration))
    finally:
        con.close()


@record(output_to_console)
def random_delay(min, max):
    sleep(randint(min, max))


def main():
    for _ in range(3):
        # print(random_delay.__name__)
        random_delay(3, 5)
    # for _ in range(3):
    #     # 取消掉装饰器
    #     random_delay.__wrapped__(3, 5)


if __name__ == '__main__':
    main()
