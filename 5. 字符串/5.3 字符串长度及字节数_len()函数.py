# len() 函数的基本语法格式
# len(string)

str = "http://www.baidu.com"
str_len = len(str)
print(str_len)

str1 = "abcdedfghijklmnopq"
print(len(str1))

# 计算字符串占用的字节数
str2 = "人生苦短，我用python"
byte_num = len(str2.encode())
print(byte_num)


# 计算使用GBK编码的字符串长度
byte_num = len(str2.encode('gbk'))
print(byte_num)



