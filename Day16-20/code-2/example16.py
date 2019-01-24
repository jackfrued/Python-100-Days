"""
魔术方法
如果要把自定义对象放到set或者用作dict的键
那么必须要重写__hash__和__eq__两个魔术方法
前者用来计算对象的哈希码，后者用来判断两个对象是否相同
哈希码不同的对象一定是不同的对象，但哈希码相同未必是相同的对象（哈希码冲撞）
所以在哈希码相同的时候还要通过__eq__来判定对象是否相同
"""


class Student():
    __slots__ = ('stuid', 'name', 'gender')

    def __init__(self, stuid, name):
        self.stuid = stuid
        self.name = name

    def __hash__(self):
        return hash(self.stuid) + hash(self.name)

    def __eq__(self, other):
        return self.stuid == other.stuid and \
            self.name == other.name

    def __str__(self):
        return f'{self.stuid}: {self.name}'

    def __repr__(self):
        return self.__str__()


class School():

    def __init__(self, name):
        self.name = name
        self.students = {}

    def __setitem__(self, key, student):
        self.students[key] = student

    def __getitem__(self, key):
        return self.students[key]


def main():
    # students = set()
    # students.add(Student(1001, '王大锤'))
    # students.add(Student(1001, '王大锤'))
    # students.add(Student(1001, '白元芳'))
    # print(len(students))
    # print(students)
    stu = Student(1234, '骆昊')
    stu.gender = 'Male'
    # stu.birth = '1980-11-28'
    print(stu.name, stu.birth)
    school = School('千锋教育')
    school[1001] = Student(1001, '王大锤')
    school[1002] = Student(1002, '白元芳')
    school[1003] = Student(1003, '白洁')
    print(school[1002])
    print(school[1003])


if __name__ == '__main__':
    main()

