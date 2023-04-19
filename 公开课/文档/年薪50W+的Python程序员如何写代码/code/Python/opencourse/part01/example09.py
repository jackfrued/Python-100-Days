import copy


class PrototypeMeta(type):

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.clone = lambda self, is_deep=True: \
            copy.deepcopy(self) if is_deep else copy.copy(self)


class Student(metaclass=PrototypeMeta):
    pass


stu1 = Student()
stu2 = stu1.clone()
print(stu1 == stu2)
print(id(stu1), id(stu2))
