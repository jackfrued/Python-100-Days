class Student(object):

    def __init__(self, id, name, age, sex):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')

    def watch_av(self):
        if self.age >= 18:
            print(f'{self.name}正在观看岛国片.')
        else:
            print(f'{self.name}只能看《熊出没》.')


def main():
    dict1 = {
        'id': 1001,
        'name': '王大锤',
        'age': 15,
        'sex': True
    }
    stu = Student(**dict1)
    stu.study('Python程序设计')
    stu.watch_av()


if __name__ == '__main__':
    main()
