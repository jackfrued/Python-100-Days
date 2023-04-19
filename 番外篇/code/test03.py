from random import randint, sample

# 初始化备选红色球
red_balls = [x for x in range(1, 34)]
# 选出六个红色球
selected_balls = sample(red_balls, 6)
# 对红色球进行排序
selected_balls.sort()
# 添加一个蓝色球
selected_balls.append(randint(1, 16))
# 输出选中的随机号码
for index, ball in enumerate(selected_balls):
    print('%02d' % ball, end=' ')
    if index == len(selected_balls) - 2:
        print('|', end=' ')
print()