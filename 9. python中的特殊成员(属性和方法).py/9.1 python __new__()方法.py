# 演示一下python 中 __new__()方法的作用

# 例一：演示 __new__() 方法和 __init__() 方法的调用顺序
class Person:
    def __new__(cls, *args, **kwargs):
        print("__new__() called")
        return object.__new__(cls)                              # 如果要得到当前类的实例，应当在当前类的 __new__() 方法中调用当前类父类的__new__()方法

    def __init__(self) -> None:
        print("__init__() called")


person = Person()                       # 先输出：__new__() called, 再输出：__init__() called
print("------------------------------------------")

# 例二：演示 若 __new__() 方法中返回的不是当前类的实例对象，则当前类的 __init__() 方法将不会调用
class Student:
    def __new__(cls, *args, **kwargs):
        print("Student's __new__() method called")
        return object.__new__(cls)

    def __init__(self) -> None:
        print("Student's __init__() method called")

class Dog:
    def __new__(cls, *args, **kwargs):
        print("Dog's __new__() called")
        return object.__new__(Student, *args, **kwargs)

    def __init__(self) -> None:
        print("Dog's __init__() called")

dog = Dog()
print(type(dog))                                # 输出:   <class '__main__.Student'>, 可以看到定义的是 Dog类，但输出的却是 Student类，且Dog类的构造方法不会被调用        

'''
输出：

Dog's __new__() called
<class '__main__.Student'>

'''


'''
总结：python中 __new__()方法的使用注意事项：

1. __new__()方法始终都是【静态方法】，因此可以不加 @staticmethod 装饰器；
2. __new__()方法必须提供一个 cls 参数，用于指代当前类对象, 也必须要有一个返回值 因为该方法的主要作用就是用于创建对象的；
3. __new__()方法的返回值可以是当前类的实例对象，也可以是其它类的实例对象，当返回的是其它类的实例对象时，将不会调用后续的 __init__()方法；
4. 与__init__()方法的区别，__new__()方法用于创建对象，__init__()方法用于初始化对象，__new__() 方法总是先于__init__()方法调用；


'''

'''
参考链接：

1. [[Python] Python 之 __new__() 方法与实例化](https://www.cnblogs.com/ifantastic/p/3175735.html)
2. [Python 类中__new__ 和 __init__方法区别](https://zhuanlan.zhihu.com/p/21379984)
'''