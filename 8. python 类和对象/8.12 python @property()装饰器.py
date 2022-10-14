# python 中的property() 装饰器
# 感觉还是没什么卵用呀......

class Student:

    def __init__(self, name) -> None:
        self.__name = name

    @property
    def name(self):
        return self.__name


student = Student("Mira")
print("student的当前名称是：", student.name)                    # student的当前名称是： Mira

# 注意：这里在Student类名没有定义setter()方法，所以直接给__namn 属性赋值也没有效果
student.__name = "Collapse"
print("student的当前名称是：", student.name)                    # student的当前名称是： Mira

# student.name = "Collapse"
# print("student的当前名称是：", student.name)                    # AttributeError: can't set attribute 'name'

class Person:
    def __init__(self, name) -> None:
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        self.__name = 0
    
person = Person("Yatoro")
print("person's name: ", person.name)                   # 输出：person's name:  Yatoro

# 更新person'name的名称：
person.name = "ANA"
print("person's name: ", person.name)                   # 输出：person's name:  ANA

# 删除person's name的名称
del person.name
print("删除后的name为：", person.name)                   # 输出：删除后的name为： 0




