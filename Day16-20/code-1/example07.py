"""
元类 - 设计模式 - 单例模式(让一个类只能创建唯一的实例)
"""


class SingletonMeta(type):
    """单例类的元类(描述其他类的类)"""

    def __init__(cls, *args, **kwargs):
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President(metaclass=SingletonMeta):
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


if __name__ == '__main__':
    main()
