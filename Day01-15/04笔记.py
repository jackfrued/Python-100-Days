# 测试一下倒计时的range()是不是前闭后开区间 ——答案：是的
sum = 0
for x in range(6, 2, -2):
    sum += x
print(sum)
"""
```

需要说明的是上面代码中的`range(1, 101)`可以用来构造一个从1到100的范围，当我们把这样一个范围放到`for-in`循环中，
就可以通过前面的循环变量`x`依次取出从1到100的整数。当然，`range`的用法非常灵活，下面给出了一个例子：

- `range(101)`：可以用来产生0到100范围的整数，需要注意的是取不到101。
- `range(1, 101)`：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
- `range(1, 101, 2)`：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
- `range(100, 0, -2)`：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。
"""

# 下面这个东西可以产生随机数
# answer = random.randint(1, 100)
# 不过检错说这个random没有定义

"""
上面的代码中使用了`break`关键字来提前终止循环，需要注意的是`break`只能终止它所在的那个循环，
这一点在使用嵌套的循环结构（下面会讲到）需要引起注意。
除了`break`之外，还有另一个关键字是`continue`，它可以用来放弃本次循环后续的代码直接让循环进入下一轮。
"""

"""
输出乘法口诀表(九九表)

Version: 0.1
Author: 骆昊
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t') # 这里的\t应该就是换行了
    print()

# 测试下运算符
print(16//2)


#练习1
"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""
x = int(input('请输入一个数：'))
i =int(1)
while i<=x:
    if i%x==0:
        break
    i +=1
if i <x:
    print('不是素数')
else :
    print('是素数')

'''
#### 练习3：打印如下所示的三角形图案。

```
*
**
***
****
*****
```

```
    *
   **
  ***
 ****
*****
```

```
    *
   ***
  *****
 *******
*********
```
'''

# 参考答案：

"""
打印三角形图案

Version: 0.1
Author: 骆昊
"""

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()



