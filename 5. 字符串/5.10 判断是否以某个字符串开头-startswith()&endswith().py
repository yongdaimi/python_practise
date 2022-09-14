# 用于判断字符串是否以某个字符开头或结束
str = "http://www.baidu.com"
result = str.startswith("http")
print(result) # 输出True

# 判断某个字符串是否以.com结尾
str = "http://www.baidu.com"
result = str.endswith(".com")
print(result) # 输出True

# 判断某个字符串是否以http开头，从指定位置开始检索, 这里是从t这个字符开始检索
str = "http://www.baidu.com"
result = str.startswith("http", 1)
print(result) # 输出False

# 判断是否以.cn结尾
str = "http://www.baidu.com"
result = str.endswith(".cn")
print(result) # 输出False
