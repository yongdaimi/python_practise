# sorted() 函数的语法如下：

# list = sorted(iterable, key=None, reverse=False)  
# - iterable 代表要排序的序列
# - key 代表排序的条件
# - reverse 代表是按升序还是降序进行排序, 默认false 为升序

# 例一：对列表进行排序
list1 = [1, 3, 21, 2, 34, 0, 20, 90, 100]
list2 = sorted(list1)
print(list2) # 输出：[0, 1, 2, 3, 20, 21, 34, 90, 100], 升序排列

list2 = sorted(list1, reverse=True)
print(list2) # 输出：[100, 90, 34, 21, 20, 3, 2, 1, 0], 降序排列

# 例二：对元组进行排序
print(sorted((1, 9, 4, 7, 10, 2))) # 输出：[1, 2, 4, 7, 9, 10]


# 例三: 对字典进行排序 (字典默认会按key进行排序)
my_dict = {3:4, 0:4, 8:3, 1:1, 16:0, 6:1}
print(sorted(my_dict)) # 输出：[0, 1, 3, 6, 8, 16]

# 例四：对字符串进行排序
name = "51423"
name1 = sorted(name)
print(name1) # 输出：['1', '2', '3', '4', '5'], 使用sorted()函数对原序列进行排序，并不会修改原序列

# 例五：使用key参数指定排序规则
chars = ['http://www.baidu.com',\
    'http://www.taobao.com', \
    'http://www.qq.com', \
    'http://www.163.com',
    'http://www.sohu.com']

print(sorted(chars, key=lambda x:len(x))) # 自定义按照字符串的长度进行排序







