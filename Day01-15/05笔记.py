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
