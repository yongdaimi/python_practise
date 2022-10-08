# 如果函数体内部仅包含一条函数语句，则可以写成lambda表达式的形式， 语法如下：
# name = lambda [list] : 表达式

# name 是 lambda表达式的名称，[list] 代表参数列表(实际书写时不需要加)， 表达式就是函数体内的具体内容


# 例一：计算两数的和
add = lambda a, b : a + b
print("10 + 5 = ", add(10, 5))


# 例二: 输出一条测试语句
print_ret = lambda : print("This is a test func")
print_ret()





