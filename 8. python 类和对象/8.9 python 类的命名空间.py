# 类中定义的成员和函数只是因为限定在类这个命名空间中，其它的与定义在类外的全局函数
# 没有什么不同

name = "lisi"
address = "广东省深圳市"

class Person:
    name = "zhangsan"
    address = "广州市天河区"

# 直接打印类变量
print("Person->name: ", Person.name)
print("Person->address: ", Person.address)


# 直接在类中执行for循环代码块

class Student:
    for i in range(10):
        print("i = ", i)

'''
输出结果：

Person->name:  zhangsan
Person->address:  广州市天河区
i =  0
i =  1
i =  2
i =  3
i =  4
i =  5
i =  6
i =  7
i =  8
i =  9

'''