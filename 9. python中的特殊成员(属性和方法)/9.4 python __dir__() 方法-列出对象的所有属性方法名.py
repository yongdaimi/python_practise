# __dir__() 方法可以列出对象的所有属性和方法名

# 例：

class Person:
    
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def say(self):
        print("说话")

    def sing(self):
        print("唱歌")

    def dance(self):
        print("跳舞")

person = Person("zhangsan", "广东")
print(person.__dir__())

'''
输出：

['name', 'address', '__module__', '__init__', 'say', 'sing', 'dance', 
'__dict__', '__weakref__', '__doc__', '__new__', '__repr__', '__hash__', 
'__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', 
'__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce_ex__', 
'__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']

'''

# 使用dir() 方法也可以达到类似的效果，dir() 方法相当于是对 __dir__() 方法做了封装，并做了排序

print(dir(person))

'''
输出：
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
 'address', 'dance', 'name', 'say', 'sing']
'''
