"""
单元测试 - 针对程序中最小的功能模块（函数和方法）的测试
测试方法：
- 白盒测试：程序自己写的测试
- 黑盒测试：测试人员或QA，不知道代码实现细节，只关注功能
编写Python单元测试 - 定义类继承TestCase，写测试方法(test_开头)
执行单元测试：
- unittest.main()
- python3 -m unittest test_example01.py
第三方库 - nose2 / pytest
pip install pytest pytest-cov
pytest -v --cov
------------------------------
pip install nose2 cov-core
nose2 -v -C
"""
from unittest import TestCase

from example01 import seq_search, bin_search


class TestExample01(TestCase):
    """测试查找函数的测试用例"""

    # 执行每个测试函数之前要执行的方法
    def setUp(self):
        self.data1 = [35, 97, 12, 68, 55, 73, 81, 40]
        self.data2 = [12, 35, 40, 55, 68, 73, 81, 97]

    # 执行每个测试函数之后要执行的方法
    def tearDown(self):
        pass

    def test_seq_search(self):
        """测试顺序查找"""
        self.assertEqual(0, seq_search(self.data1, 35))
        self.assertEqual(2, seq_search(self.data1, 12))
        self.assertEqual(6, seq_search(self.data1, 81))
        self.assertEqual(7, seq_search(self.data1, 40))
        self.assertEqual(-1, seq_search(self.data1, 99))
        self.assertEqual(-1, seq_search(self.data1, 7))

    def test_bin_search(self):
        """测试二分查找"""
        self.assertEqual(1, bin_search(self.data2, 35))
        self.assertEqual(0, bin_search(self.data2, 12))
        self.assertEqual(6, bin_search(self.data2, 81))
        self.assertEqual(2, bin_search(self.data2, 40))
        self.assertEqual(7, bin_search(self.data2, 97))
        self.assertEqual(-1, bin_search(self.data2, 7))
        self.assertEqual(-1, bin_search(self.data2, 99))
