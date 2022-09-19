# 其中的 ch 为迭代变量，in 关键字后面可以跟 列表、元组、字符串、字典、集合等序列类型

# 遍历字符串
from unittest import result


url = "http://www.baidu.com"
for ch in url:
    print("%c" %ch, end="") # 输出：http://www.baidu.com

# 遍历range()函数生成的结果
print("计算从1到100的结果...")
result = 0
for i in range(101): # range()函数是python的内置函数，用于生成一系列连续整数
    result += i
print(result) # 输出5050

# 遍历列表
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
for i in my_list:
    print("%d, " %i, end="") # 输出：1, 2, 3, 4, 5, 6, 7, 8,

print("\n")


# 遍历字典
my_dict = {
    "百度":"http://www.baidu.com",\
    "腾讯":"http://www.qq.com",\
    "网易":"http://www.163.com"
}

for dic in my_dict:
    print(dic, end="\n") # 输出：百度腾讯网易, 注意：默认只输出 keys 的集合

for dic in my_dict.values():
    print(dic, end=" ") # 输出: http://www.baidu.com http://www.qq.com http://www.163.com

for dic in my_dict.items():
    print(dic, end=" ") # 输出：('百度', 'http://www.baidu.com') ('腾讯', 'http://www.qq.com') ('网易', 'http://www.163.com') 





