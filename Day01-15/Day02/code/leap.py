"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\或()折行
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)
