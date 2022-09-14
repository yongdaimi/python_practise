# 去字符串左右两侧的空格及特殊字符 这里的特殊字符，指的是制表符（\t）、回车符（\r）、换行符（\n）等。

str = "     http://www.baidu.com    \r\n"
str1 = str.strip()
print(str1) # 输出：http://www.baidu.com

# 去除左侧的空格及特殊字符
str = "     http://www.baidu.com    \r\n"
str1 = str.lstrip()
print(str1) # 输出：http://www.baidu.com 注意：右侧其实还是有制表符及换行符标记的，可以从控制台看出


# 去除右侧的空格及特殊字符
str = "     http://www.baidu.com    \r\n"
str1 = str.rstrip()
print(str1) # 输出：     http://www.baidu.com




