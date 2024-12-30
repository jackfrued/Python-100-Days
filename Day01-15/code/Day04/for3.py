"""
输入非负整数n计算n!

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

n = int(input('n = '))
result = 1
for x in range(1, n + 1):
    result *= x
print('%d! = %d' % (n, result))
print('{}! = {}'.format (n ,result))
print('{0}! = {1}'.format (n ,result))
print('{n1}! = {result1}'.format (n1 = n ,result1 = result))

# 格式化输出1
hobby = input('请输入你的爱好:')
s = '爱好{hobby},性别{}'.format('男',hobby = hobby)
# s = '爱好{hobby},性别{}'.format(hobby = hobby, '男')  # 报错，命名的参数需放最后
print(s)

# 格式化输出2
s1 = '爱好{},性别{}'.format('发呆','男')   # 正确
s2 = '爱好{0},性别{1}'.format('发呆','男')   # 正确
# s = '爱好{},性别{1}'.format('发呆','男')   # 报错，索引不可与默认格式混合使用
print(s1)

# 格式化输出3
char = '性别{s[1]}'.format(s = '1男生1')    # 索引对参数的部分进行取值，s[1]=='男'
print(char)

# 格式化输出4
s11 = 'π是{:.2f}'.format(3.1415926)
print(s11)
s22 = 'π是%.2f'% 3.1415926
print(s22)

# {:1}指截取索引为[0:1]的字符（顾头不顾尾）
s = '性别{:.1}'.format('男生122')
# {:2}指截取索引为[0:2]的字符（顾头不顾尾）
m = '性别{:.2}'.format('男生122')
print(s)
print(m)

# 格式化输出5
s = "{:*^10}".format('12345')   # 通过（: 符号^数字）进行字符串的填充，数字为填充后的字符串总长度
print(s)

s = "{:-^20}".format('123456')
print(s)
# 数字{要求的长度}小于字符串的长度，则不进行填充操作