# 演示python 类变量和实例变量

#==========================================================================
# 什么是【类变量】?
# 在类体中，所有函数之外，在此范围定义的变量，称为【类属性】或【类变量】
#==========================================================================


class Person: 
    name = "zhangsan"           # 类变量
    age = 20                    # 类变量

    def say(self):
        print("%s说了一句话" %self.name)

# 1. 打印类变量的值
print(Person.name) # 输出：zhangsan
print(Person.age)  # 输出：20


# 2. 修改类变量的值
Person.name = "lisi"
Person.age = 17
print(Person.name) # 输出：lisi
print(Person.age)  # 输出：17

'''
可以看到，通过类名不但可以调用类变量，也可以修改类变量的值
也可以使用类对象来调用所属类中的类变量，但是强烈不推荐!!!
'''

# 3. 由于类变量是所有类共有，因此修改类变量的值，会影响所有的实例化对象
# 通过类名修改类对象，会作用到所有的实例化对象

print("------------ 修改前类变量的值 -----------")
person1 = Person()
person2 = Person()
print("person1->name: ", person1.name)
print("person1->age: ", person1.age)
print("person2->name: ", person2.name)
print("person2->age: ", person2.age)

print("------------ 修改后类变量的值 -----------")
Person.name = "ana"
Person.age = 20
print("person1->name: ", person1.name)
print("person1->age: ", person1.age)
print("person2->name: ", person2.name)
print("person2->age: ", person2.age)

'''
通过类对象是无法修改类变量的，通过类对象给类变量赋值，本质不是修改类变量的值，而是创建了一个新的实例变量
'''

# 4.可以动态地为该类添加类变量
Person.address = "广东省广州市"
print("Person's address: ", Person.address) # 输出：Person's address:  广东省广州市


#==========================================================================
# 什么是【实例变量】?
# 在类体中，所有函数内部，以"self.变量名" 定义的变量，称为【实例变量】
#==========================================================================

class School:
    name = "深圳中学"
    address = "深圳市南山区"

    def __init__(self):
        self.name = "广州中学"                   # 实例变量
        self.address = "广州市天河区"            # 实例变量

    def detail(self):
        print("当前学校的名称为：%s, 地址在：%s" %(self.name, self.address)) # 输出：当前学校的名称为：广州中学, 地址在：广州市天河区

# 1. 打印实例变量的值
high_school = School()
print(high_school.name)                         # 广州中学
print(high_school.address)                      # 广州市天河区
high_school.detail()

# 2. 为该对象添加新的实例变量
high_school.student_num = 1000  
print("当前学校的总人数：", high_school.student_num) # 输出：当前学校的总人数： 1000

# 3. 修改一个类对象的实例变量不会影响其它类对象的实例变量和这个类本身的类变量
print("------------------------- 修改类的实例变量(修改前) ------------------------------")
print("School类变量<name>: ", School.name)
print("School类变量<address>: ", School.address)
print("School实例变量[high_school]<name>: ", high_school.name)
print("School实例变量[high_school]<address>: ", high_school.address)

middle_school = School()
middle_school.name = "厦门中学"
middle_school.address = "厦门市地利区"

print("------------------------- 修改类的实例变量(修改后) ------------------------------")
print("School类变量<name>: ", School.name)
print("School类变量<address>: ", School.address)
print("School实例变量[high_school]<name>: ", high_school.name)
print("School实例变量[high_school]<address>: ", high_school.address)
print("School实例变量[middle_school]<name>: ", middle_school.name)
print("School实例变量[middle_school]<address>: ", middle_school.address)

'''
输出结果：
------------------------- 修改类的实例变量(修改前) ------------------------------
School类变量<name>:  深圳中学
School类变量<address>:  深圳市南山区
School实例变量[high_school]<name>:  广州中学
School实例变量[high_school]<address>:  广州市天河区
------------------------- 修改类的实例变量(修改后) ------------------------------
School类变量<name>:  深圳中学
School类变量<address>:  深圳市南山区
School实例变量[high_school]<name>:  广州中学
School实例变量[high_school]<address>:  广州市天河区
School实例变量[middle_school]<name>:  厦门中学
School实例变量[middle_school]<address>:  厦门市地利区
'''


#==========================================================================
# 什么是【局部变量】?
# 在所有函数内部：以“变量名=变量值”的方式定义的变量，称为【局部变量】
#==========================================================================

class MathHelper:
    def calculate(self, value):
        price = value * 0.8;                        # 局部变量
        print("这件商品打折后的价格为：", price)

pencil_price = 20
helper = MathHelper()
helper.calculate(pencil_price)                      # 输出：这件商品打折后的价格为： 16.0



