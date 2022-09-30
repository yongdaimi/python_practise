# 在python中， 函数的内部可以定义变量，还可以定义函数，在函数的内部定义的函数被称为 “局部函数 ”

# 例1：
def outdef():
    # 局部函数
    def indef():
        print("http://www.baidu.com")
    # 调用局部函数
    indef()

# 调用全局函数
outdef() # 输出：http://www.baidu.com


# 例2：
def outdef():
    # 局部函数
    def indef():
        print("局部函数被调用")
    # 调用局部函数
    return indef

# 调用全局函数
new_indef = outdef()
new_indef()

'''
关于局部函数的作用域:

如果所在函数函数没有返回局部函数，则局部函数的可用范围仅限于所在函数内部；反之， 如果所在函数将局部函数作为返回值，则局部函数的作用域就会扩大
既可以在所在函数内使用， 也可以在所在函数作用域中使用。

'''

# 例3：局部函数中定义的变量名若与外部函数同名，则会发生遮蔽

def outdef():
    name = "http://www.baidu.com"
    # 局部函数
    def indef():
        nonlocal name
        print(name)
        # name = "http://www.163.com"   # 直接这样调用是错误的，会报 variable 示定义的错误
        name = "http://www.163.com" # 若要修改外部变量的值，需要先添加 nonlocal关键字

    indef()

# 调用全局函数
outdef()

