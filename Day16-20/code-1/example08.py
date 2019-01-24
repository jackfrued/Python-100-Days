"""
设计模式 - 单例模式(让一个类只能创建唯一的实例)
"""
from functools import wraps


def singleton(cls):
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class President():
    """总统(单例类)"""

    def __init__(self, name):
        self.name = name


def main():
    p1 = President("王大锤")
    p2 = President("奥巴马")
    print(p1.name)
    print(p2.name)
    print(p1 == p2)
    print(p1 is p2)
    print('-' * 30)
    # 取消装饰器
    President2 = President.__wrapped__
    p2 = President2("奥巴马")
    print(p1.name)
    print(p2.name)
    print(p1 == p2)
    print(p1 is p2)



if __name__ == '__main__':
    main()
