# python __del__() 方法, 在对象销毁时会被调用

class Person:
    def __init__(self) -> None:
        print("Person's __init__() called")

    def __del__(self):
        print("Person's __del__() called")


person = Person()
del person

print("-------------------------------")


# 特别注意：如果我们重写了子类的__del__方法，则在销毁时也需要调用父的 __del__方法

class Man:
    def __del__(self):
        print("Man's __del__ called")

class Boy(Man):
    def __del__(self):
        print("Boy's __del__ called")

boy = Boy()
del boy                                     # 注意，这里只会输出:Boy's __del__ called, 父类的 __del__ 方法没有被调用

print("---------------------- 改造 ----------------------------")

class Man:
    def __del__(self):
        print("Man's __del__ called")

class Boy(Man):
    def __del__(self):
        super().__del__()
        print("Boy's __del__ called")

boy = Boy()
del boy                         

'''
输出：

Man's __del__ called
Boy's __del__ called

'''
