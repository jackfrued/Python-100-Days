# 序列化 - 把对象写入数据流 - 串行化 / 归档 / 腌咸菜
# 反序列化 - 从数据流中恢复出对象 - 反串行化 / 解归档
# Python有三个支持序列化的模块
# json - JSON / pickle - 二进制 / shelve
import json
import pickle


class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    list1 = [10, 'hello', 99.9, 'goodbye']
    print(json.dumps(list1))
    print(pickle.dumps(list1))
    dict1 = {'name': '骆昊', 'age': 38}
    print(json.dumps(dict1))
    print(pickle.dumps(dict1))
    stu = Student('骆昊', 38)
    print(pickle.dumps(stu))

