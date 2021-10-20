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