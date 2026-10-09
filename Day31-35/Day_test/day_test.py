


# heap = []                      # 堆就是一个普通空列表
# for x in [34, 25, 12, 99, 87]:
#     heapq.heappush(heap, x)  #压入一个元素
#     print(f'push {x} 后：{heap} 堆顶={heap[0]}')
#
# while heap:
#     smallest = heapq.heappop(heap) #弹出最小值
#     print(f'pop 得到 {smallest}，剩余：{heap}')
#

# 用push / pop 实现堆排序

# def heap_sort(items):
#     heap1 = []
#     for item in items:
#         heapq.heappush(heap1, item) #将items中的元素依次压入 heaq1 列表中
#         print(f'已压入元素 {item}，当前列表 {heap1}')
#
#     return [heapq.heappop(heap1) for _ in range(len(heap1))]
#
#
# if __name__ == '__main__':
#     data = [34, 25, 12, 99, 87, 63]
#     heap_sort(data)
#
#     print("heaq_sort: ", heap_sort(data))
#     print("sorted : ", sorted(data))

# 模拟医院叫号：压入 (紧急程度, 到达序号, 病人名)，思考为什么中间要加到达序号。

# 给你一个整数数组 salary ，数组里每个数都是 唯一 的，其中 salary[i] 是第 i 个员工的工资。
#
# 请你返回去掉最低工资和最高工资以后，剩下员工工资的平均值。

# class Solution:
#     def average(self, salary):
#         return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2.0)
#
#
# salary = [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]
# res = Solution()
# print(res.average(salary))



# print(list(itertools.permutations('ABC',2)))
#
# print(list(itertools.combinations('ABC',2)))
#
# print(list(itertools.product('ABC','12')))
#
# print(list(itertools.count(10,2)))


# 百钱买百鸡
# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只

# for x in range(20):
#     for y in range(33):
#         z = 100 -x -y
#         if 5*x + 3*y + z // 3 == 100 and z % 3 == 0:
#             print(x,y,z)

# import itertools
#
# for x, y in itertools.product(range(20), range(33)):
#     z = 100 - x - y
#     if 5*x + 3*y + z // 3 == 100 and z % 3 == 0:
#         print(x,y,z)


# import itertools
#
# # list1 = list(itertools.combinations(range(1, 34), 6))
# # print(len(list1))
#
# scores = sorted([45, 80, 59, 90, 66, 30, 100])
# for passed, group in itertools.groupby(scores, key=lambda x:x>=60):
#     print('及格' if passed else '不及格', list(group))

# file_path = '../Day_test/day31_test02.py'
# with open(file_path,"r") as f:
#     content = f.read()
#     print(content)
#     f.seek(0)
#     content1 = f.read()
#     print(content1)

# import pickle
#
#
# my_list = [1, 2, 3, '范范', [5, 6, 7]]
#
# pickle_file = open('my_list.pkl', 'wb')   # 注意：wb，二进制写
# pickle.dump(my_list, pickle_file)          # 把对象倒进文件
# pickle_file.close()
#
# pickle_file = open('my_list.pkl', 'rb')   # rb，二进制读
# my_list2 = pickle.load(pickle_file)        # 原样取回
# print(my_list2)
# pickle_file.close()

# 简单选择排序
# def select_sort(items ):
#     items = items[:]
#     for i in range(len(items) - 1):
#         min_index = i
#         for j in range(i+1, len(items)):
#             if items[j]<items[min_index]:
#                 min_index = j
#
#         items[i], items[min_index] = items[min_index], items[i]
#     return items

# 冒泡排序
# def bubble_sort(items):
#     items = items[:] #复制列表
#     for i in range(len(items)-1): #外层循环次数
#         flag = False  #设置状态位
#         for j in range(len(items)-1-i): #内层循环次数，减去i 代表最右边i个已经排好序了，不用再遍历
#             if items[j] > items[j+1]:  #判断相邻两个元素大小，
#                 items[j],items[j+1] = items[j+1],items[j] #交换值，大的右移
#                 flag = True  #改变状态位
#         # 升级版，从后往前比较。
#         if flag:
#             flag = False
#             for j in range(len(items)-1-i,i,-1):
#                 if items[j-1] > items[j]:
#                     items[j-1], items[j] = items[j], items[j-1]
#                     flag = True
#         if not flag:
#             break
#
#     return items



# 合并两个有序列表
# def merge(item1,item2,comp=lambda x, y: x < y):
#     items = []
#     index1,index2 = 0, 0
#     while index1 < len(item1) and index2 < len(item2):
#         if comp(item1[index1] , item2[index2]):
#             items.append(item1[index1])
#             index1 += 1
#         else:
#             items.append(item2[index2])
#             index2 += 1

#     items += item1[index1:]
#     items += item2[index2:]

#     return items



# if __name__ == '__main__':
#     item1 = [1,2]
#     item2 = [4,5,6,1]
#     items1 = merge(item1,item2)
#     print(items1)


# import bisect

# def ind_index(items, x):
#     i = bisect.bisect_left(items, x)
#     if i !=len(items) and items[i] == x:
#         return i

#     return -1

# if __name__ == "__main__":
#     my_list = [1,2,5,3,4,5,6,7,8,9,10]



  # A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
  # 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
  # B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
  # 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼

# fish = 6
# while True:
#     total = fish
#     flag = True
#     for _ in range(5):
#         if (total - 1) % 5 == 0:
#             total = (total - 1) // 5 * 4
#         else:
#             flag = False
#             break
#     if flag:
#         print(fish)
#         break
#     fish += 5


# def main():
#     """贪婪法：背包问题 - 单函数实现"""
#     # 物品数据：(名称, 价格, 重量)
#     all_things = [
#         ('电脑', 200, 20),
#         ('收音机', 20, 4),
#         ('钟', 175, 10),
#         ('花瓶', 50, 2),
#         ('书', 10, 1),
#         ('油画', 90, 9),
#     ]
#     max_weight = 20

#     # 按性价比（价格/重量）降序排列
#     all_things.sort(key=lambda x: x[1] / x[2], reverse=True)
#     total_weight, total_price = 0, 0
#     for name, price, weight in all_things:
#         if total_weight + weight <= max_weight:
#             print(f"小偷拿走了：{name}")
#             total_weight += weight
#             total_price += price
#     print(f"总价值：{total_price}美元")


# if __name__ == "__main__":
#     main()



# 在柠檬水摊上，每一杯柠檬水的售价为 5 美元。顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

# 每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

# 注意，一开始你手头没有任何零钱。

# 给你一个整数数组 bills ，其中 bills[i] 是第 i 位顾客付的账。如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

 

# 示例 1：

# 输入：bills = [5,5,5,10,20]
# 输出：true
# 解释：
# 前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
# 第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
# 第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
# 由于所有客户都得到了正确的找零，所以我们输出 true。

# class Solution(object):
#     def lemonadeChange(self, bills):
#         """
#         :type bills: List[int]
#         :rtype: bool
#         """
#         five, ten = 0, 0  # 只需记录5元和10元的张数
#         for bill in bills:
#             if bill == 5:
#                 five += 1
#             elif bill == 10:
#                 if five < 1:
#                     return False
#                 else:
#                     five -= 1
#                     ten += 1
#             elif bill == 20:
#                 if ten >= 1 and five >= 1:
#                     ten -= 1
#                     five -= 1
#                 elif five >=3:
#                     five -= 3
#                 else:
#                     return False
#         return True
# # 测试
# s = Solution()
# print(s.lemonadeChange([5, 5, 5, 10, 20]))     # True
# print(s.lemonadeChange([5, 5, 10, 10, 20]))     # False
# print(s.lemonadeChange([5, 5, 10, 20, 5, 5]))   # True

        

# from itertools import combinations


# class Solution(object):
#     def largestPerimeter(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort(reverse=True)  # 降序排列
#         for i in range(len(nums) - 2):
#             # 只需检查：两短边之和 > 最长边
#             if nums[i + 1] + nums[i + 2] > nums[i]:
#                 return nums[i] + nums[i + 1] + nums[i + 2]
#         return 0

#     def allTriangles(self, nums):
#         """找出所有能组成三角形的组合"""
#         result = []
#         for a, b, c in combinations(sorted(nums), 3):
#             # 排序后 a ≤ b ≤ c，只需检查 a + b > c
#             if a + b > c:
#                 result.append((a, b, c))
#         return result


# # 测试
# s = Solution()
# print("最大周长:", s.largestPerimeter([2, 1, 2]))        # 5
# print("所有组合:", s.allTriangles([2, 1, 2]))            # [(1, 2, 2)]
# print("所有组合:", s.allTriangles([3, 6, 2, 3]))         # [(2, 3, 3), (3, 3, 6)]
# print("所有组合:", s.allTriangles([1, 2, 1, 10]))        # []
# print("所有组合:", s.allTriangles([3, 4, 5, 6, 7]))      # 多个


# items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
# items2 = [x ** 2 for x in range(1, 10) if x % 2]
# print(items1)
# print(items2)

# import time
# from functools import wraps

# def record_time(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         print(f'{func.__name__}执行了: {time.time() - start}秒')
#         return result

#     return wrapper

# @record_time
# def slow_add(a, b):
#     time.sleep(2)
#     return a + b

# res = slow_add(1,3)
# print(res)

# 装饰器案例1，权限管理。
# from functools import wraps
# current_user = {'username':'fan', 'is_admin':False}

# def require_admin(func):
#     """只允许管理员操作"""
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if not current_user.get('is_admin'):
#             raise PermissionError("403 Forbidden: 权限不足，仅管理员可操作！")

#         return func(*args, **kwargs)
#     return wrapper


# @require_admin
# def delete_database():
#     print('数据库已成功删除！')

# try:
#     delete_database()
# except PermissionError as e:
#     print(f"拦截成功：{e}")



# 装饰器案例2：网络请求自动重试

# import time
# from functools import wraps

# def retry(max_times=3, delay=1):
#     """模拟失败自动重连装饰器"""
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             for attempt in range(1, max_times + 1):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as err:
#                     print(f"第 {attempt} 次尝试失败: {err}")
#                     if attempt == max_times:
#                         raise
#                     time.sleep(delay)
#         return wrapper
#     return decorator

# count = 0
# @retry(max_times=3, delay=0.5)
# def fetch_api_data():
#     global count
#     count += 1
#     if count < 5:
#         raise ConnectionError("网络连接超时")
#     return {"status": 200, "data": "请求成功"}

# print("最终结果:", fetch_api_data())


# 练习 1：通用参数与日志打印器 @log_call（基础）
# 训练重点：掌握 *args、**kwargs、返回值传递与 @wraps。
# 业务需求： 编写一个装饰器 @log_call，在函数执行前打印出调用的函数名以及收到的所有参数，在执行后打印出该函数的返回值。


# from functools import wraps

# def log_call(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'[调用] {func.__name__} 传入参数：args={args}, kwargs={kwargs}')
#         result =   func(*args, **kwargs)
#         print(f'[返回] {func.__name__} 执行结果：{result}')
#         return result
#     return wrapper

# @log_call
# def add(a, b):
#     return a + b
# res = add(10, 20)


# 练习 2：防止暴力点击的冷却限制器 @cooling_down(seconds)（带参数装饰器）
# 训练重点：掌握 3 层嵌套闭包与状态保留。
# 业务需求： 在网页或游戏开发中，防止玩家/用户在短时间内频繁点击按钮（如发送验证码）。 
# 编写一个带参数的装饰器 @cooling_down(seconds)，规定 seconds 秒内该函数只能成功执行 1 次。
# 如果在冷却期内再次调用，则拦截并提示 f"请等待 {剩余秒数:.1f} 秒后再试"，且不执行原函数。

# import time
# from functools import wraps


# def cooling_down(seconds):
#     def cool_down(func):
#         last_aclled = 0 #设置基准，上次调用默认为0
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             nonlocal last_aclled
#             #开始时间
#             start = time.time()
#             # 距离上次调用过了多久
#             elapsed = start - last_aclled
#             # 判断是否还在冷却中
#             if elapsed < seconds:
#                 print(f"请等待 {seconds - elapsed:.1f} 秒后再试")
#                 return None
            
#             # 超过冷却时间，允许执行，并更新上次调用时间
#             last_aclled = start
#             return func(*args, **kwargs)
#         return wrapper
#     return cool_down


# @cooling_down(seconds=2)
# def send_sms(phone):
#     print(f"成功向 {phone} 发送验证码！")

# send_sms("13800138000")  # 立即执行
# time.sleep(1.1)
# send_sms("13800138001")  # 立即再次调用 -> 拦截并提示冷却中！
# time.sleep(2.1)
# send_sms("13800138002")  # 2秒后调用 -> 正常执行

# 练习 3：函数返回值校验与转换器 @returns(target_type)（进阶）
# 训练重点：对原函数的返回值进行捕获、验证与二次加工。
# 业务需求： 某些接口要求函数无论内部怎么计算，最终必须返回指定类型（如 int、str 或 list）。 编写一个装饰器 @returns(target_type)：
# 如果函数的返回值本身就是 target_type，直接返回；
# 如果不是，尝试使用 target_type(result) 强转；
# 如果强转失败，则抛出 TypeError(f"返回值无法转换为 {target_type.__name__}")。

from functools import wraps

def returns(target_type):
    def returning(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if type(result) == target_type:
                return result
            try:
                return target_type(result)
            except(ValueError, TypeError):
                raise TypeError(f"返回值无法转换为 {target_type.__name__}")
        return wrapper
    return returning

@returns(int)
def get_id():
    return "12345"  # 原本是字符串

res = get_id()
print(res, type(res))  # 输出: 12345 <class 'int'>

@returns(int)
def get_bad_id():
    return "hello"  # 字符串 hello 无法转换成 int

get_bad_id()
