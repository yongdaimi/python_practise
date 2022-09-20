# 元组是放到小括号里面的一组数据，用逗号分隔
tuple1 = ("ana", "topson", "ceb", "jerex", "notail") # 使用小括号()可以直接创建元组
print(tuple1) # 输出：('ana', 'topson', 'ceb', 'jerex', 'notail')
print(type(tuple1)) # 输出：<class 'tuple'>


# python元组可以存放任意类型的数据(如下：依次存放：字符串、列表、元组、字典)
tuple1 = ("ana", [1, 2, 3, 4, 5], ("maybe", "ame"), {'beijing':"100", 'shanghai':"20"})
print(tuple1) # 输出：('ana', [1, 2, 3, 4, 5], ('maybe', 'ame'), {'beijing': '100', 'shanghai': '20'})


# 注意：小括号不是必须的，只要使用逗号,将元素隔开，python就会将其视为一个元组
tuple1 = "ana", "topson", "ceb", "jerex", "notail"
print(tuple1) # 输出：('ana', 'topson', 'ceb', 'jerex', 'notail')
print(type(tuple1)) # 输出：<class 'tuple'>


# 注意：当元组中只有一个字符串元素时, 需要给该元素后面添加一个逗号，否则python会将该元组视为一个字符串
# 有加逗号
tuple1 = ("http://www.baidu.com",)
print(tuple1)       # 输出：('http://www.baidu.com',)
print(type(tuple1)) # 输出：<class 'tuple'>

# 不加逗号
tuple1 = ("http://www.baidu.com")
print(tuple1)       # 输出：http://www.baidu.com
print(type(tuple1)) # 输出：<class 'str'>


def print_ele_type(a):
    print(a)
    print(type(a))

#===============================================================
#       使用tuple()内置函数来创建元组,语法：tuple(data)
#===============================================================
# 将字符串转换为元组
a = tuple("http://www.baidu.com") 
print_ele_type(a) # 输出：('h', 't', 't', 'p', ':', '/', '/', 'w', 'w', 'w', '.', 'b', 'a', 'i', 'd', 'u', '.', 'c', 'o', 'm')


# 将列表转换为元组
a = tuple([1, 2, 3, 4, 5])
print_ele_type(a) # 输出：(1, 2, 3, 4, 5)

# 将字典转换为元组
a = tuple({'henan':"zhengZhou", 'jiangsu':"nanjing"})
print_ele_type(a) # 输出：('henan', 'jiangsu'), 只会输出key

# 将区间转换为元组
a = tuple(range(1, 6))
print_ele_type(a) # 输出: (1, 2, 3, 4, 5)

# 创建空元组
a = tuple()
print_ele_type(a) #输出：()


#==========================================================
#                       访问元组元素
#==========================================================
url = tuple("http://www.baidu.com")

print(url[3]) # 输出p
print(url[-4]) # 输出.

# 使用切片访问元组中的一组元素
print(url[5:8]) # 输出：('/', '/', 'w')

# 指定步长
print(url[4:12:2]) # 输出：(':', '/', 'w', '.')


#==========================================================
#                       修改元组
#==========================================================
tup = (100, 0.5, -36, 64)
print(tup)
tup = (42, 43, 4343, 4343 , 43431, 24)
print(tup)
# tup[2] = 50 # 元组是只读的，不允许被修改
print(tup)

# 拼接两个元组会生成新元组
tup1 = ("ana", "topson")
tup2 = ("ceb", "jearex", "notail")
tup3 = tup1 + tup2
print(tup1)
print(tup2)
print(tup3)
print(tup1 == tup3) # 输出False


#==========================================================
#                       删除元组
#==========================================================
tup = ('C', 'C++')
print(tup)
del tup
print(tup) # 删除之后，解释器会报：name 'tup' is not defined, python 解释器自带垃圾回收，一般不需要主动删除





