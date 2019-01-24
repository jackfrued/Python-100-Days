"""
装饰器 - 背后的设计模式是代理模式(注意不是装饰器模式)
代理模式通常是让代理对象去执行被代理对象的行为并在这个过程中增加额外的操作
这种设计模式最适合处理代码中的横切关注功能(与正常业务没有必然联系但是又需要执行的功能)
"""
from functools import wraps
from time import time


def record(output=print):
    
    def decorate(func):
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            output(func.__name__, time() - start)
            return result
            
        return wrapper
    
    return decorate


@record()
def some_task():
    print(123 ** 100000)


if __name__ == '__main__':
    some_task()
    print(some_task.__name__)
    # 取消装饰器
    some_task = some_task.__wrapped__
    some_task()
