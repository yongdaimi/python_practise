# ====================================================
#               例一：使用python 类对象
# ====================================================

class Person:
    name = "no name"
    age = 20
    height = 1.8

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about(self):
        print(self.name, " 的年龄是：", self.age, " 身高是：", self.height)

    def say(self, content):
        print(content)

person = Person("Zhangsan", 20)
person.about() # 输出：Zhangsan  的年龄是： 20  身高是： 1.8

# 修改 name 和 age
person.name = "lisi"
person.age = 50
person.about() # 输出：lisi  的年龄是： 50  身高是： 1.8

person.say("HAHAWTF") # 输出：HAHAWTF



# ==========================================================
#               例二：给类对象动态添加/删除属性
# ==========================================================
person.weight = 50
print("%s的体重是%d千克" %(person.name, person.weight)) # 输出：lisi的体重是50千克

# 删除新添加的weight属性
# del person.weight
# print("%s的体重是%d千克" %(person.name, person.weight)) # 输出: 错误：'Person' object has no attribute 'weight'. Did you mean: 'height'?



# ==========================================================
#               例三：给类对象动态添加成员方法
# ==========================================================

'''
做法一: 直接使用函数赋值
'''
# 1. 先定义一个需要绑定到python对象上的函数
def address_info(self):
    print("我家的地址是在GuangDong, GuangZhou")

# 2. 再将该函数赋值给python对象上，这个成员可以没有
person.address = address_info

# 3. 注意：当在python对象上调用这个新添加的方法时，还需要将python对象传入
person.address(person) # 输出：我家的地址是在GuangDong, GuangZhou

'''
做法二：使用lambda函数赋值
'''
person.animal = lambda self : print("最爱的动物是小猫")
person.animal(person) # 输出：最爱的动物是小猫


'''
如果不想在调用方法时传入调用的python对象，可以使用MethodType将调用的方法进行二次包装
'''

# 导入 MethodType
from types import MethodType

def hobby_info(self, content):
    print("我的爱好是：", content)

person.hobby = MethodType(hobby_info, person)
person.hobby("打篮球") # 输出：我的爱好是： 打篮球




