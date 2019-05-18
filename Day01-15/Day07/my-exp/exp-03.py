"""
Author: Tang

Date:2019-05-18

设计一个函数返回传入的列表中最大和第二大的元素的值。
"""
def get_max(num):
    num = sorted(num, reverse=True)
    return num[0],num[1]


if __name__=="__main__":
    lis = [2,3,1,8,4,6,9]
    m1, m2 = get_max(lis)
    print(lis)
    print(m1, m2)