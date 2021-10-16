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
