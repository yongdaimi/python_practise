# 查找该字符串中是否包含字符.
str = "http://www.baidu.com"
num = str.index('.')
print(num) # 输出10


# 查找该字符串是否包含字符.(从右侧开始检索)
str = "http://www.baidu.com"
num = str.rindex('.')
print(num) # 输出16


# 查找该字符串是否包含指定字符 * 
str = "http://www.baidu.com"
num = str.rindex('*')
print(num) # 会抛出异常: substring not found

'''
结论：
index()函数与find()函数最大的区别就是前者在查找时，如果找不到指定的字符会抛出异常
'''





