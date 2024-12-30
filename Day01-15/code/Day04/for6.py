"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):      # '_'在下面的循环体中不会被用到，只是起到控制循环次数的作用
        print('*', end='')
    print()     # 起到Enter的作用

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')  # 若不加end，则自动换行
        else:
            print('*', end='')
    print()     # 起到Enter的作用

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()     # 起到Enter的作用
