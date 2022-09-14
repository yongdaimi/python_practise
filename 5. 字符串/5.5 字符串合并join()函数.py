# join()方法用于将列表或元组中的多个字符串使用特定的分割符连接成一个新的字符串
# 语法：newstr = str.join(iterable)

# 将列表中的字符串拼接成一个新的字符串
list1 = ['www','baidu','com']
str = '.'.join(list1)
print(str) # 输出：www.baidu.com

# 将元组中的字符串拼接成一个新的字符串
dir = '','usr','bin','env'
print(type(dir))
str = '/'.join(dir)
print(str) # 输出：/usr/bin/env
