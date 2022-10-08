# 演示闭包函数的用法
# 闭包函数中外部函数返回的是函数名, 而不是某个值

def format_str(str1):
    def inner_format():
        return "============= "+str(str1)+" ================"
    return inner_format

a = format_str(20)

print(a())


# 例二: 输入任意一个数，对输入的数进行加上指定的数

def outer_func(a):
    def inner_func(b):
        print("outer_func: input value: %d, inner_func: input value: %d" %(a, b))
        return a + b
    return inner_func

a = outer_func(4)

# 对4 加2
print("4 + 2 = ", a(2))

# 对4 加3
print("4 + 3 = ", a(3))

# 对4 加8
print("4 + 8 = ", a(8))


#===============================================================
#           python 闭包的 __closure__属性
#===============================================================
# 闭包比普通函数多了一个 __closure__ 属性, 该属性记录着自由变量的地址。当闭包被调用时，系统会根据该地址找到对应的自由变量，完成整体的函数调用。
# 这里的自由变量指的就是【外部函数中的参数】

# 查看上述outer_func()函数中参数a的地址：
print(a.__closure__)

