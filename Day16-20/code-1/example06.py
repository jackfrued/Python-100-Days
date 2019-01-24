"""
抽象类 / 继承 / 多态
"""
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪"""
        pass


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000


class Programmer(Employee):
    """程序员"""

    def __init__(self, name):
        super().__init__(name)
        self._working_hour = 0

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, _working_hour):
        self._working_hour = 0 if _working_hour < 0 \
            else _working_hour

    def get_salary(self):
        return 200 * self.working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name):
        super().__init__(name)
        self._sales = 0

    @property
    def sales(self):
        return self._sales
    
    @sales.setter
    def sales(self, _sales):
        self._sales = 0 if _sales < 0 else _sales

    def get_salary(self):
        return 1800 + 0.05 * self.sales


def main():
    """主函数"""
    emps = [
        Programmer("王大锤"), Manager("武则天"),
        Programmer("狄仁杰"), Salesman("白洁"),
        Programmer("白元芳"), Salesman("冷面")
    ]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = int(input(f'{emp.name}本月工作时间: '))
        elif isinstance(emp, Salesman):
            emp.sales = float(input(f'{emp.name}本月销售额: '))
        print("%s本月工资为: ￥%.2f元" % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
