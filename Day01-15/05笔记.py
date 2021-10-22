# 练习1 水仙花数
for num in range(100,1000):
    low = num % 10
    high = num // 100
    mid = num % 100 // 10
    # mid = num // 10 % 10
    if low**3 + high**3 + mid**3 == num:
        print('%d是水仙花数' % num) # 正确格式
    # else print('%d不是水仙花数',(num))

# 练习1 附加练习：数字颠倒顺序：
num = int(input('请输入一个多位正整数：'))
num_reversed = 0
while num > 0:
    num_reversed = num_reversed*10 + num%10
    num //= 10
print(num_reversed)

# 练习2 百钱百鸡
for x in range(0,21): # 本题不考虑21也是可以的，因为这种情况凑不满100只鸡
    for y in range(0,34):
        # for z in range(0,301):
        z = 100 - x -y
        if 5*x + 3*y + z/3 == 100:
            print('买%d只公鸡，%d只母鸡，%d只小鸡' % (x,y,z))

for xx in range(0,3):
    print(xx)

'''   
上面使用的方法叫做**穷举法**，也称为**暴力搜索法**，
这种方法通过一项一项的列举备选解决方案中所有可能的候选项并检查每个候选项是否符合问题的描述，
最终得到问题的解。这种方法看起来比较笨拙，但对于运算能力非常强大的计算机来说，
通常都是一个可行的甚至是不错的选择，而且问题的解如果存在，这种方法一定能够找到它。
'''

# 练习3 CRAPS赌博游戏
# 由于游戏规则较为复杂且难于验证，因此我这里仅给出伪代码：
from random import randint
money = 1000
while money > 0:
    # 【结构】第一种死循环直到输出正确结果的办法：
    while True: # 【注意】大写开头的True才是逻辑值
        debt = int(input('请下赌注：'))
        if 0<debt<=money:
            break

    print('玩家要出了%d点：' % debt)

    first = randint(1,6) + randint(1,6) # 相当于摇两次色子求和

    # 【结构】判断是否进入下一次循环的办法：
    needs_go_on = False
    if 2<1:
        print('玩家胜!')
    elif 1>2:
        print('玩家胜!')
    else:
        needs_go_on = True
    # 【结构】第二种死循环直到输出正确结果的办法：
    
    while needs_go_on:
        needs_go_on = False
        if 5<3:
            print('玩家胜!')
        elif 3>5:
            print('玩家胜!')
        else:
            needs_go_on = True
print('你破产了, 游戏结束!')

# 【说明】本程序一共三次循环，满足条件方才进入下一次循环。
# 上一次的循环产生的结果可以作为下一次循环是否开始的逻辑判断条件
# 也可以作为自身是否继续循环的条件


# 有用的练习1~3

# 有用的练习1：生成**斐波那契数列**的前20个数

''''
a = 1
b = 1
 for _in range(0,20): # 这里的_仅用于计数
     a,b = b,a+b
     print(b,end = ' ')
'''
# 标准答案：
a = 0 # 这里把序列号排到了没有加运算之前
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')


# 有用的练习2：找出10000以内的**完美数**
import math

for num in range(0,10001):
    result = 0
    # for factor in range(1,math.sqrt(num)+1):
    for factor in range(1,int(num)+1):
        if num % factor == 0:
            result += factor
    if num == result:
        print(num)

'''
标准答案这部分，用了平方减小循环，并利用互补的因子直接求出大因子，这是利用了因式分解的互补特性。
下面是标准答案
'''
import math

for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)

# 练习3：输出**100以内所有的素数**
import math
for num in range(2,101):
    # for factor in range(2,math.sqrt(num)+1):
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            break
    if factor == int(math.sqrt(num)):
        print(num,end=' ')

# 标准答案（修改）：

import math

for num in range(2, 100):
    # is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
        #    is_prime = False
            break
    #if is_prime:
    if factor == int(math.sqrt(num)):
        print(num, end=' ')