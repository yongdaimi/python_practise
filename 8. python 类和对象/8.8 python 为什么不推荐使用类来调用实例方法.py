# 本文解释一下为什么不推荐使用类来调用实例方法

class Person:

    def __init__(self):
        self.name = "XiaoMing"

    def print_name(self):
        print("当前Person的名称为：", self.name)


class Dog:
    pass

dog = Dog()


# 通过类对象调用实例方法
person = Person()
person.print_name()                 # 输出：当前Person的名称为： XiaoMing


# 通过类调用实例方法
Person.print_name(dog)              # 输出：'Dog' object has no attribute 'name'


'''
可以看到， 通过类来调用实例方法时，需要传入一个实例对象，但是python却不对实例对象进行检查，如果传入的实例
对象不是调用类的所对应的实例对象，那么运行时就会出错，上面在调用时需要传入Person 类的实例对象 person，而不是
传入Dog类的实例对象dog

上面代码运行时会报错：

AttributeError: 'Dog' object has no attribute 'name'

'''