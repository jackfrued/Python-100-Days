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

"""
for i in range(1,6):
    i += 1
    for j in range(1,i):
        print('*', end = " ")
    print()

for i in range(1,6):
    for j in range(1,6 - i + 1):
        print(" ", end = ' ')
    for j in range(1, i + 1):
        print('*', end = ' ')
    print()

for i in range(1,6):
    for j in range(1, 6 - i - 1): 
        print(" ", end = "")
    for j in range(1, 2 * i):
        print('*', end = '')
    print()
