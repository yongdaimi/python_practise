# python __dict__属性可以访问一个类里面的所有类属性和实例属性
# 注意：__dict__ 是属性，不是方法！

# 例一：使用__dict__属性访问类里的所有类属性和实例属性

class Person:
    age = 20
    address = "广东省天河区"

    def __init__(self) -> None:
        self.name = "zhangsan"
        self.sex = "男"

    def say(self):
        print("他说了一句话")

print("--------------------------------- 由类调用 --------------------------------")
print(Person.__dict__)

'''
输出：

{'__module__': '__main__', 'age': 20, 'address': '广东省天河区', '__init__': <function Person.__init__ at 0x000002222439A0E0>, 'say': <function Person.say at 0x000002222439A170>, 
'__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}


注意看：它返回的是一个字典，但是也是可以访问到成员函数的

'''

# 例二：如果是类调用，则能访问到所有的类属性；如果是对象调用，则能访问到所有的实例属性
print("--------------------------------- 由对象调用 ------------------------------")
person = Person()
print(person.__dict__)

'''
输出

{'name': 'zhangsan', 'sex': '男'}
'''


# 例三：子类只能访问到它自身的类属性或实例属性，无法访问其父类的类属性或实例属性
class Son(Person):
    hobby = "猫"
    ball = "篮球"

    def __init__(self) -> None:
        self.mother = "Mother"
        self.father = "Father"

    def sing(self):
        print("会唱歌")

print("--------------------------------- Son类调用 __dict__ ------------------------------")
print(Son.__dict__)


'''
输出：

{'__module__': '__main__', 'hobby': '猫', 'ball': '篮球', '__init__': <function Son.__init__ at 0x0000022C2BB9A290>, 'sing': <function Son.sing at 0x0000022C2BB9A320>, '__doc__': None}


'''

print("--------------------------------- Son对象调用 __dict__ ------------------------------")
son = Son()
print(son.__dict__)

'''
输出：

{'mother': 'Mother', 'father': 'Father'}
'''


# 例四：可以通过 __dict__ 来修改类的实例属性，但是无法通过它来修改类属性

# 修改实例属性
print("修改person对象的实例属性 name ")
person.__dict__['name'] = "Topson"
print(person.__dict__)

'''
输出：
{'name': 'Topson', 'sex': '男'}
'''

# 修改类属性
print("修改person对象的实例属性 age ")
Person.__dict__['age'] = 40
print(Person.__dict__)

'''
输出：

会直接报错：
'mappingproxy' object does not support item assignment

'''