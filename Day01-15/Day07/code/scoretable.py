"""
学生考试成绩表

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    subjs = ['语文', '数学', '英语']
    scores = [[0] * 3] * 5
    for row, name in enumerate(names):
        print('请输入%s的成绩' % name)
        for col, subj in enumerate(subjs):
            scores[row][col] = float(input(subj + ': '))
    print(scores)
#   for row, name in enumerate(names):
#       print('请输入%s的成绩' % name)
#       scores[row] = [None] * len(subjs)
#       for col, subj in enumerate(subjs):
#           score = float(input(subj + ': '))
#           scores[row][col] = score
#   print(scores)

if __name__ == '__main__':
    main()
