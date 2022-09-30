# python 中函数还可以作为参数和返回值，使用起来有点像是指针调用

#============================================================
#                  直接将函数赋值给变量
#============================================================

def print_test():
    print("This is a test func")

a = print_test # 将函数名直接赋值给变量
a() # 输出：This is a test func


#============================================================
#                  将函数作为参数
#============================================================

def sum(a, b):
    print("a + b = ", a + b)

def product(a, b):
    print("a * b = ", a * b)

def get_result(func, a , b):
    func(a, b)

# 求和
get_result(sum, 3, 4)                           # 输出：a + b =  7
# 求积  
get_result(product, 3, 4)                       # 输出：a * b =  12


#============================================================
#                  将函数作为返回值
#============================================================

def math_test():
    print("enter math test func... ")
    def power(a):
        result = a ** 2
        print("%d ** 2 = %d" %(a, result))      # 输出：8 ** 2 = 64
    return power(8)

math_test()


def math_test_2():
    print("enter math test func... ")
    def power():
        print("calling power() func")      
    return power

a = math_test_2()                           
a()                                             # # 输出：calling power() func


#============================================================
#            将函数赋值给变量时加括号与不加括号的区别
#============================================================

def test():
    print("call the test func")
    return 0

p = test
print("type(p): ", type(p))

print('----------------------------------')

p = test()
print("type(p): ", type(p))

# 相当于是给print()函数取了一个别名
p = print
p("oh, oh, oh")

