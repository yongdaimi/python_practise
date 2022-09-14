# 统计某个字符在指定字符串中出现的次数


# 统计 . 在字符串http://www.baidu.com中出现的次数
str = "http://www.baidu.com"
num = str.count('.')
print(num) # 输出：2


str = "http://www.baidu.com."
num = str.count('.')
print(num) # 输出：3


# 从索引号为10的位置开始检索, 索引号为10的位置就是第一次出现.的位置, 从指定位置开始检索，会包含起始位置
str = "http://www.baidu.com"
num = str.count('.', 10)
print(num) # 输出：2

# 从索引号为11的位置开始检索, 即;从字符b开始检索
str = "http://www.baidu.com"
num = str.count('.', 11)
print(num) # 输出：1

# 从索引号为11~16的位置进行检索, 即: 起始位置是字符b, 结束位置是第二个.号的位置
str = "http://www.baidu.com"
num = str.count('.', 11, 16)
print(num) # 输出：0

# 从索引号为11~17的位置进行检索, 即: 起始位置是字符b, 结束位置是字符c
str = "http://www.baidu.com"
num = str.count('.', 11, 17)
print(num) # 输出：1

'''
结论：
count() 函数检索的范围包含起始位置，但是不包含结束位置
'''


