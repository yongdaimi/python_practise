
'''
Hello 模块

有一个公共的函数：speaking(), 当在其它模块中调用本模块时，这个函数会自动执行
本模块提供了一个类：Student, 可以对该类进行实例化
'''

def speaking():
    print("say hello world")

speaking()

class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def say(self):
        print("我是%s, 我已经%d岁了" %(self.name, self.age))


if __name__ == '__main__':                          # __name__是python的内置属性，如果是在当前模块中执行代码时，它为 __main__
    student = Student("张三", 20)
    student.say()

