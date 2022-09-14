# ljust(), rjust(), center() 可以通过给字符串填充指定的字符以达到对齐效果
str = "http://www.baidu.com"
str1 = "http://www.a.cn"

# 将总字符长度填充到35个字符，以达到左对齐效果
l_str = str.ljust(35)
l_str1 = str1.ljust(35)
print(l_str)
print(l_str1)

print('==========================')
r_str = str.rjust(35)
r_str1 = str1.rjust(35)
print(r_str)
print(r_str1)


# 以指定的字符进行填充,上面没有指定填充字符，所以默认使用的空格
# 这里指定使用*号进行填充
l_str = str.ljust(35, '*')
l_str1 = str1.ljust(35, '*')
print(l_str)      # 输出：http://www.baidu.com***************
print(l_str1)     # 输出：http://www.a.cn********************


# 使文本居中
c_str = str.center(35, '-')
c_str1 = str1.center(35, '-')
print(c_str)     # 输出：--------http://www.baidu.com-------
print(c_str1)    # 输出：----------http://www.a.cn----------

