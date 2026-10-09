# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }



# for key, value in prices.items():
#     if value > 100:
#         print(f"{key} {value}")

# prices2 = {key: value for key, value in prices.items() if value > 100}
# print(prices2)
# # 用股票价格大于100元的股票构造一个新的字典
# # prices2 = {key: value for key, value in prices.items() if value > 100}
# # print(prices2)
# - 嵌套的列表的坑

# import openpyxl
# from pathlib import Path
# file_path = Path(__file__).parent / '考试成绩表A.xlsx'

# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# # 录入五个学生三门课程的成绩
# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))


# # 写入Excel
# wb = openpyxl.Workbook()

# sheet = wb.active
# sheet.title = '期末成绩'

# sheet.cell(1, 1, '姓名')  # A1单元格
# for col_index, course in enumerate(courses):
#     sheet.cell(1, col_index + 2, course)

# for row_index, name in enumerate(names):
#     sheet.cell(row_index + 2, 1, name)

#  #          ↑ 行（从第2行开始）  ↑ 列（从第2列开始）  ↑ 取出对应成绩
# for row_index, name in enumerate(names):
#     for col_index, course in enumerate(courses):
#         sheet.cell(row_index + 2, col_index + 2, scores[row_index][col_index])

# wb.save(file_path)



# import itertools

# # 产生ABCD的全排列
# itertools.permutations('ABCD')
# # 产生ABCDE的五选三组合
# itertools.combinations('ABCDE', 3)
# # 产生ABCD和123的笛卡尔积
# itertools.product('ABCD', '123')
# # 产生ABC的无限循环序列
# itertools.cycle(('A', 'B', 'C'))

# comp匿名函数：比较两个值，如果 x < y 返回 True，否则返回 False
# def select_sort(items, comp=lambda x, y: x < y):
#     # 复制列表，排序变动不影响原列表
#     items = items[:]
#     # 以列表索引循环遍历
#     for i in range(len(items) - 1):
#         # 设置最小值的索引
#         min_index = i
#         # 从第一个元素和后面的比较
#         for j in range(i + 1, len(items)):
#             # 调用匿名函数，更新最小值索引 # 比较items[j]和当前最小值，如果更小则更新最小值索引
#             if comp(items[j], items[min_index]):
#                 min_index = j
#         # 调换位置，最小值放在前面
#         items[i], items[min_index] = items[min_index], items[i]
#     return items

# items = [5,3,6,8,2,1]
# res = select_sort(items)
# print(res)


  # 公鸡5元一只 母鸡3元一只 小鸡1元三只
  # 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只

# for x in range(20):
#     for y in range(33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
#             print(x,y,z)



  # A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
  # 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
  # B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
  # 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼

# fish = 6
# while True:
#     total = fish
#     enough = True
#     for _ in range(5):
#         if (total - 1) % 5 == 0:
#             total = (total - 1) // 5 * 4
#         else:
#             enough = False
#             break

#     if enough:
#         print(fish)
#         break
#     fish += 5


# class Thing(object):
#     """物品"""

#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight

#     @property
#     def value(self):
#         """价格重量比"""
#         return self.price / self.weight
    
# def input_thing():
#     """输入商品信息"""
#     name_str, price_str, weight_str = input().split()
#     return name_str, int(price_str), int(weight_str)

# def main():
#     """主函数"""
#     max_weight, num_of_things = map(int, input().split())
#     all_things = []
#     for _ in range(num_of_things):
#         all_things.append(Thing(*input_thing()))

#     all_things.sort(key=lambda x: x.value, reverse=True)
#     total_weight = 0
#     total_price = 0
#     for thing in all_things:
#         if total_weight + thing.weight <= max_weight:
#             print(f'小偷拿走了{thing.name}')
#             total_price += thing.price
#             total_weight += thing.weight

#     print(f'总价值: {total_price}美元')

# if __name__ == '__main__':
#     main()
# items1 = list(map(lambda x :x**2,
#                   filter(lambda x : x%2, range(1,10))))

# nums = range(1,21)
# result = list(filter(lambda x : x % 2, nums))
# print(result)

# 从列表中筛选出大于等于 60 的分数。
# scores = [45, 80, 59, 90, 66, 30, 100]
# result = list(filter(lambda x : x >= 60, scores))
# print(result)
# new_result = sorted(result)
# print(new_result)

# result2 = [x for x in scores if x >= 60]
# print(result2)
# 从名字列表中筛选出长度大于 3 的名字。
# names = ['Tom', 'Jack', 'Amy', 'Tony', 'Alex']
# new_names = [x for x in names if len(x) > 3]
# print(new_names)

# new_names1 = list(filter(lambda x: len(x) > 3, names))
# print(new_names1)

# map 练习：只转换
# map 用来“把每个数据加工成另一个数据”。

# 把 1 ~ 10 每个数字变成平方。
# nums = list(map(lambda x: x**2, range(1,11)))
# print(nums)
# # 把分数列表全部加 5 分。
# scores = [45, 80, 59, 90, 66]
# result = list(map(lambda x: x + 5, scores))
# print(result)
# # 把名字列表全部转成大写。
# names = ['tom', 'jack', 'amy']
# new_names = list(map(lambda x : x.upper(), names))
# print(new_names)


# 三、map + filter 综合练习/
# 先 filter 筛选，再 map 转换。
# 从 1 ~ 20 中筛选出奇数，然后求平方。
# list = list(map(lambda x : x ** 2, filter(lambda x : x % 2, range(1,21))))
# print(list)

# 从分数中筛选出及格分数，然后全部加 10 分。
# scores = [45, 80, 59, 90, 66, 30, 100]
# new_scores = list(map(lambda x : x+10, filter(lambda x : x >= 60, scores)))
# print(new_scores)

# 从名字中筛选出以 a 开头的名字，然后转成首字母大写。
# names = ['alice', 'bob', 'anna', 'tom', 'alex']
# new_names = list(map(lambda name : name.title(), filter(lambda name : name.startswith('a'), names)))
# print(new_names)


# 练习1：从 nums 中筛选出能被 3 整除的数字
# 目标：[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# nums = range(1, 31)

# new_nums = list(filter(lambda x : x % 3 == 0, nums))
# print(new_nums)

# 练习2：把 nums 中每个数字变成它的立方

# 目标：[1, 8, 27, 64, 125]
# nums = range(1, 6)
# new_nums = list(map(lambda num : num ** 3, nums))
# print(new_nums)

# 练习3：从 nums 中筛选出偶数，然后把偶数乘以 10

# 目标：[20, 40, 60, 80, 100]
# nums = range(1, 11)
# new_nums = list(map(lambda num :num * 10, filter(lambda x : x%2==0, nums)))
# print(new_nums)

# filter 负责筛选
# map 负责加工

# list(map(加工规则, filter(筛选规则, 数据)))
# from functools import wraps
# from time import time, sleep

# def record_time(func):
#     """自定义装饰函数的装饰器"""
    
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         print(f'{func.__name__}: {time() - start}秒')
#         return result
        
#     return wrapper


# @record_time
# def download():
#     sleep(1)
#     return '下载完成'


# print(download())


# 练习 1：最基础的计时装饰器
# 写一个装饰器 record_time，统计函数执行时间。
# 要求：

# from functools import wraps
# from time import time, sleep


# def record(func):
    
#     @wraps(func)
#     def wrapper(*agrs, **kwargs):
#         start = time()
#         result = func(*agrs, **kwargs)
#         print(f'{func.__name__}: {time() - start}秒')
#         return result
#     return wrapper

# @record
# def task():
#     sleep(1)
#     return '任务完成'
# print(task())

# 练习 3：打印函数开始和结束
# 写一个装饰器 log_func，在函数执行前打印“开始执行”，执行后打印“执行结束”。

# from functools import wraps
# from time import sleep, time


# def log_func(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'{func.__name__}: 开始执行')
#         start = time()
#         result = func(*args, **kwargs)
#         print(f'{func.__name__}: {time() - start}秒')
#         print(f'{func.__name__}: 执行结束')
#         return result
#     return wrapper



# @log_func
# def download():
#     sleep(1)
#     return '下载完成'

# print(download())


# 练习 5：统计函数被调用次数
# 写一个装饰器 count_calls，统计某个函数被调用了几次。
# 要求：

# from functools import wraps


# def count_calls(func):
#     count = 0

#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f'第{count}次调用 {func.__name__}')
#         result = func(*args, **kwargs)
#         return result
#     return wrapper





# @count_calls
# def say_hello():
#     print('hello')

# say_hello()
# say_hello()
# say_hello()


# 面向对象知识：
"""
工资结算系统
不同员工类型工资不同，使用工厂模式创建不同的员工对象

"""

# from abc import ABCMeta, abstractmethod


# class Employee(metaclass=ABCMeta):
#     """员工抽象类"""
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def get_salary(self):
#         pass

# class Manager(Employee):
#     """部门经理"""
#     def get_salary(self):
#         return 15000.0

# class Programmer(Employee):
#     """程序员"""
#     def __init__(self, name, work_hour=0):
#         super().__init__(name)
#         self.work_hour = work_hour

#     def get_salary(self):
#         return 200.0 * self.work_hour


# class Salesman(Employee):
#     """销售员"""
#     def __init__(self, name, sales=0.0):
#         super().__init__(name)
#         self.sales = sales

#     def get_salary(self):
#         return 1800.0 + self.sales * 0.05


# class EmployeeFactory:
#     """创建员工的工厂（工厂模式-通过工厂实现对象使用者和对象之间的解耦和"""

#     @staticmethod
#     def create(emp_type, *args, **kwargs):
#         """创建员工"""
#         all_emp_types = {'M':Manager,'P':Programmer,'S':Salesman}
#         cls = all_emp_types.get(emp_type.upper())
#         return cls(*args, **kwargs) if cls else None


# def main():
#     """主函数"""
#     emps = [
#         EmployeeFactory.create('m','张三'),
#         EmployeeFactory.create('p','李四', 120),
#         EmployeeFactory.create('p','王五', 85),
#         EmployeeFactory.create('s','马六', 120000),
#     ]
#     for emp in emps:
#         print(f'{emp.name}工资: {emp.get_salary():.2f}元')


# if __name__ == '__main__':
#     main()




# 学生选课
class Student:
    def __init__(self,name):
        self.name = name
        self.courses = []
        self.grades = {}

    def __repr__(self):
        return self.name

    @property
    def total_credit(self):
        return sum(c.credit for c in self.courses)

    def enroll(self, course):
        if course in self.courses:
            print(f'{self.name}已经选过{course}')
            return
        if course.is_full:
            print(f'{course} 容量{course.capacity}课程已满。')
            return
        if self.total_credit + course.credit > 20:
            print(f'{self.name}加上这门课会超过20，不用再修。')
            return
        self.courses.append(course)
        course.students.append(self)


class Course:
    def __init__(self,name,credit,capacity):
        """
        课程名称、学分、课程容量
        """
        self.name = name
        self.credit = credit
        self.capacity = capacity
        self.students = []

    def __repr__(self):
        return self.name

    @property
    def is_full(self):
        return len(self.students) >= self.capacity

class Teacher:
    def __init__(self, name):
        self.name = name

    def assign_grade(self, student, course, score):
        student.grades[course] = score

class School:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.students = []

    def create_course(self, name, credit, capacity):
        """创建课程
        名称、学分、容量
        """
        course = Course(name, credit, capacity)
        self.courses.append(course)
        return course

    def show_course(self):
        """显示学校当前所有课程"""
        if not self.courses:
            print('当前没有课程。')
            return

        print(f'{self.name}当前开设的课程：')
        for index, course in enumerate(self.courses, start=1):
            print(
                f'{index}. {course.name}，'
                f'学分：{course.credit}，'
                f'容量：{course.capacity}，'
                f'已选人数：{len(course.students)}'
            )

    def add_student(self, student):
        """增加学生"""
        return self.students.append(student)


if __name__ == '__main__':
    # 重复选课
    python = Course('python', 1, 30)
    alice = Student('Alice')
    alice.enroll(python)
    alice.enroll(python)
    print(alice.courses)
    print(python.students)

    # 课程选满
    tiny = Course('tiny', 2, 1)
    alice.enroll(tiny)
    bob = Student('Bob')
    bob.enroll(tiny)

    # 学分超限
    big1 = Course('big1', 10, 30)
    big2 = Course('big2', 10, 30)
    bob.enroll(big1)
    bob.enroll(big2)
    bob.enroll(python)
    print(bob.courses, bob.total_credit)

    # 创建课程
    school = School('school')
    school.create_course('math', 10, 20)
    print(school.courses)

