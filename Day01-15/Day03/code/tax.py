"""
输入月收入和五险一金计算个人所得税
说明：依据最新个人所得税法，个税免征额为 5000 元

Version: 0.2
Author: 骆昊
Date: 2019-05-21
"""

salary = float(input('本月收入: '))
insurance = float(input('五险一金: '))
diff = salary - insurance - 5000
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 3000:
    rate = 0.03
    deduction = 0
elif diff < 12000:
    rate = 0.1
    deduction = 210
elif diff < 25000:
    rate = 0.2
    deduction = 1410
elif diff < 35000:
    rate = 0.25
    deduction = 2660
elif diff < 55000:
    rate = 0.3
    deduction = 4410
elif diff < 80000:
    rate = 0.35
    deduction = 7160
else:
    rate = 0.45
    deduction = 15160
tax = abs(diff * rate - deduction)
print('个人所得税: ￥%.2f元' % tax)
print('实际到手收入: ￥%.2f元' % (diff + 5000 - tax))
