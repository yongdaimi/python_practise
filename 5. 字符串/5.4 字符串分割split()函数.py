# 采用默认分割符进行分割
str = "百度官方网站 >>> http://www.baidu.com"
list1 = str.split() # 默认使用空格进行分割， 输出：['百度官方网站', '>>>', 'http://www.baidu.com']
print(list1)

str = "百度官方网站>>>http://www.baidu.com"
list1 = str.split() # 默认使用空格进行分割，输出：['百度官方网站>>>http://www.baidu.com']
print(list1)

# 使用 >>> 进行分割
str = "百度官方网站>>>http://www.baidu.com"
list1 = str.split('>>>') # 输出：['百度官方网站', 'http://www.baidu.com']
print(list1)

# 使用 . 进行分割
str = "百度官方网站>>>http://www.baidu.com"
list1 = str.split('.') # 输出：['百度官方网站>>>http://www', 'baidu', 'com']
print(list1)

# 使用空格进行分割
str = "百度 官方 网站 >>> http://www.baidu.com"
list1 = str.split(' ') # 输出：['百度', '官方', '网站', '>>>', 'http://www.baidu.com']
print(list1)

# 使用空格进行分割，并且最多只分割成2个子串
str = "百度 官方 网站 >>> http://www.baidu.com"
list1 = str.split(' ', 2) # 输出：['百度', '官方', '网站 >>> http://www.baidu.com']
print(list1)

# 使用 > 进行分割
str = "百度官方网站>>>http://www.baidu.com"
list1 = str.split('>') # 输出：['百度官方网站', '', '', 'http://www.baidu.com']
print(list1)

###########################################################################
# 注意:未指定分割参数时,会使用空字符进行分割，字符串有连续的空格或其它的
# 的空字符时，也会被视为一个分割符对字符串进行分割
###########################################################################
str = "百度官方网站                 >>>                          http://www.baidu.com" # 包含多个连续的空格
list1 = str.split()
print(list1) # 输出：['百度官方网站', '>>>', 'http://www.baidu.com']







