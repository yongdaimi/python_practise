# 连续书写形式拼接字符串
str1 = "http://www.baidu.com""http://wwww.taobao.com"
print(str1)

# 使用变量
str2 = "abc"
str3 = "dfg"
str4 = str2 + str3
print(str4)

# 使用+号也能拼接字符串
str5 = "http://www.baidu.com" + "http://www.qq.com"
print(str5)


# 与数字拼接(需要使用str()或repr()函数)
name = "zhangSan"
age = 20
info = name + "已经" + str(age) + "岁了"
print(info)

name = "Lisi"
age = 28
info = name + "已经" + repr(age) + "岁了"
print(info)


# str() 与 repr() 区别
s = "http://www.baidu.com"
s_str = str(s)
s_repr = repr(s)
print(type(s_str))
print(s_str)
print(type(s_repr))
print(s_repr)







