# 函数式编程特点：
# 允许把函数本身作为参数传入另一个函数，还允许返回一个函数
# python 对函数式编程的支持主要包括以下三个函数：
# - map()
# - filter()
# - reduce()

# ======================================================
#                   将函数名作为参数
# ======================================================

def sum_operation(x, y):
    return x + y

def reduce_operation(x, y):
    return x - y

def multiple_state_func(func, x, y):
    return func(x, y)

# 计算 3 + 5 的和
print("3 + 5 = ", multiple_state_func(sum_operation, 3, 5))

# 计算 3 - 5 的差
print("3 - 5 = ", multiple_state_func(reduce_operation, 3, 5))


# ======================================================
#                   python 函数式编程
# ======================================================

# map() - 对列表中的数据循环执行相同的操作

# 例一：将列表中的所有元素都乘以 2
list1 = [1, 3, 5, 7, 9]
new_list = map(lambda x : x*2, list1)
print("type: ", type(new_list)) # 输出：type:  <class 'map'>
print(list(new_list)) # 输出：[2, 6, 10, 14, 18]

'''
注意：
1. map()函数的作用相当于是对可迭代对象中的子元素多次执行同一操作，这个可迭代对象可以是列表或是字符串; 
2. map()函数的返回值是map对象，不能直接输出，所以上面使用list()函数进行转换。
3. 可迭代对象可以是多个
'''

# 例二：将两个列表中对应位置的元素相乘
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
new_list = map(lambda x, y: x*y, list1, list2)
print(list(new_list)) # 输出：[2, 12, 30, 56, 90]


# filter() - 对迭代器中的每个元素，都使用指定的函数进行判断，并返回True或False, 最后将返回True的元素组成一个新的可遍历的集合

# 例三：返回所有网址中以.cn结尾的网址
tuple1 = ("http://www.baidu.com", 
        "http://www.qq.com", 
        "http://www.cntv.cn", 
        "http://www.163.com", 
        "http://www.yunduan.cn", 
        "http://www.google.cn")

result = filter(lambda str : str.endswith(".cn"), tuple1)
print("type(result): ", type(result)) # 输出：type(result):  <class 'filter'>
print(tuple(result)) # 输出：('http://www.cntv.cn', 'http://www.yunduan.cn', 'http://www.google.cn')


# reduce() - 对迭代器中的集合做累积操作, 注意：不是求积

# 例四：计算列表中所有元素的积
import functools
list1 = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x *y, list1)
print("type(result): ", type(result)) # 输出：type(result):  <class 'int'>
print(result) # 输出：120


# 例四：计算列表中所有元素的和
result = functools.reduce(lambda x, y: x + y, list1)
print("type(result): ", type(result)) # 输出：type(result):  <class 'int'>
print(result) # 15


'''
注意点：

1. python 3.x 中已移除了reduce()函数，使用前需要先引入 functools 模块；
2. reduce() 函数中的函数参数必须是一个包含2个函数的参数; 
'''

'''
应用场景：
如果需要对集合中的元素应用一些简单操作(如：累加、累乘), 应优先使用map(), filter(), reduce()来实现；
另外，在数据量比较多的情况下(如：机器学习应用)，一般更倾向于函数式编程的操作，因为效率更高
'''






