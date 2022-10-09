# python 规定， 在定义类的过程中， 不管是显式的创建类的构造方法，还是向类中添加实例方法，
# 都要求将self参数作为方法的第一个参数。

class Person:

    name = None
    age = None
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print("%s的年龄是%d岁" %(self.name, self.age))

person = Person("张麻子", 20)
person.print_info() # 张麻子的年龄是20岁

p = person.print_info
p() # 张麻子的年龄是20岁
