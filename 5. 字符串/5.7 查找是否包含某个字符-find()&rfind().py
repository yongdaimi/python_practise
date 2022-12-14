# 判断字符串是否包含.号, 如果包含则返回该字符第一次出现的索引位置，否则返回-1
str = "http://www.baidu.com"
num = str.find('.')
print(num) # 输出10

# 从指定的位置开始检索，从字符b开始检索
num = str.find('.', 11)
print(num) # 输出16

# 指定起始位置和结束位置进行检索
num = str.find('.', 11, 16)
print(num) # 输出-1

num = str.find('.', 11, 17)
print(num) # 输出16

# rfind()从右侧开始检索，find()默认从左侧开始检索, 注意从右侧开始检索时，返回的索引号仍然是从左侧0开始的索引号，比如这里会返回16
str = "http://www.baidu.com"
num = str.rfind('.')
print(num) # 输出16


'''
结论：
当检索到指定字符时会返回该字符出现的位置索引
若指定开始位置和结束位置，则会包含起始位置，但不会包括结束位置
'''

