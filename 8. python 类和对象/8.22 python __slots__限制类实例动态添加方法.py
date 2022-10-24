# 为类动态 实例方法、静态方法、类方法

class Person:
    pass

def say(self):
    print("实例方法-说话")

def info(self):
    print("实例方法-打印当前信息")

@classmethod
def dance(cls):
    print("类方法-跳舞")

@staticmethod
def eat():
    print("静态方法-吃东西")

# 为类动态添加类方法，会影响所有该类的实例对象
Person.say = say
Person.dance = dance
Person.eat = eat

# person 对象已拥有上述三个方法
person = Person()
person.say()
person.dance()
person.eat()

'''
输出：

实例方法-说话
类方法-跳舞
静态方法-吃东西

'''

# 允许为类对象动态添加实例方法
person2 = Person()
person2.info = info
person2.sbc = dance

person2.info(person2)           # 注意：调用时必须传入对象本身
# person2.sbc()                 # 不允许为实例对象动态添加类方法或静态方法


print("-------------------使用 __slots__ 属性限制动态地为实例对象添加属性和方法 ----------------------------------")

def address(self):
    print("地址是在：河北省正定县")

def school(self):
    print("他所在的学校是：清华大学")

class Student:
    __slots__ = ('name', 'sex', "address")


stu = Student()

# 允许动态为其添加 name 属性
stu.name = "zhangsan"
# 允许动态为其添加 address 方法
stu.address = address

stu.address(stu)
print("student's name: ", stu.name)


# 不允许动态为其添加 money 属性，因为在 __slotes__ 中没有配置该属性, 会报：'Student' object has no attribute 'money' 的错误
# stu.money = 200
# print("student's money: ", stu.money)


# 不允许为其动态添加 school 方法，因为在 __slots__ 属性中没有配置
# stu.school = school
# stu.school(stu)




print("-------------------  __slots__ 属性只对实例对象有用，不能限制类对象 ----------------------------------")


@classmethod
def dance(cls):
    print("会跳舞")

# 为Student 类动态添加 dance 方法
Student.dance = dance
stu1 = Student()

stu1.dance() # 会跳舞


print("-------------------  __slots__ 属性只对当前实例对象有用, 对子类的实例对象无用 ----------------------------------")

class HighSchoolStudnet(Student):
    pass

def sing(self):
    print("会唱歌")


# 创建 Student 类的子类 HighSchoolStudnet 对象， 并为其添加 sing 方法
stu2 = HighSchoolStudnet()
stu2.sing = sing
stu2.sing(stu2)                 # 输出：会唱歌， 可以看到，它并未受到父类中定义的 __slots__ 属性影响


'''
总结： 
    1. __slots__ 属性可以限制为实例对象动态添加属性和方法
    2. __slots__ 属性只能对实例对象起作用，对类对象无效
    3. __slots__ 属性只对当前类的实例对象起作用，对子类的实例对象无用，若想对子类的实例对象起作用，需要在子类的实例对象中再次定义

'''



