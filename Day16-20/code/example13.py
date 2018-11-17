"""
魔术方法 - 哈希存储 / 上下文语法
"""
from random import randint


class Student():
    """学生"""

    def __init__(self, stuid, name, gender):
        self.stuid = stuid
        self.name = name
        self.gender = gender

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        pass

    def __hash__(self):
        return hash(self.stuid)

    def __eq__(self, other):
        return self.stuid == other.stuid

    def __repr__(self):
        return f'{self.stuid}: {self.name}'


def create_student():
    return Student(randint(1001, 9999), 
                   "无名氏", 
                   "男" if randint(0, 1) == 1 else "女")


def main():
    """主函数"""
    students = {
        Student(1001, "王大锤", "男"),
        Student(1001, "王小锤", "男"),
        Student(1003, "王捶捶", "女")
    }
    print(len(students))
    print(students)
    with create_student() as stu:
        print(stu.stuid)
        print(stu.name)
        print(stu.gender)


if __name__ == '__main__':
    main()
