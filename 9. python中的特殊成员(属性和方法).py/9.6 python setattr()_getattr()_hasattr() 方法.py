# 演示下python的getattr(), setattr(), hasattr() 方法, 这三个函数是python的内置函数
# 这些方法能用来判断python 类中是否包含某个属性，获取某个属性的值，设置某个属性的值

# ===================================================
#                   hasattr()函数
#     用于判断某个类的实例对象是否指定名称的属性和方法, 返回值是True 或 False,
#     但是它只能判断有还是没有，不能区分到底是属性还是方法
# =====================================================

class Person:
    name = "zhangsan"
    age = 40

    def __init__(self) -> None:
        self.address = "广东省天河区"
        self.sex = "男"

    def sayHello(self):
        print("Hello world")


person = Person()
print(hasattr(person, "name"))          # True
print(hasattr(person, "age"))           # TRUE
print(hasattr(person, "address"))      # True
print(hasattr(person, "sex"))           # True
print(hasattr(person, "sayHello"))      # True
print(hasattr(person, "skip"))          # False


# ==============================================================
#                   getattr函数
#  语法格式：getattr(__o: object, __name: str, __default: None)
#
# ==============================================================


# 取得 name 属性和 age 属性的值
print("-------------------- get attribute value -------------------------")
# 输出: person的名称是： zhangsan
print("person的名称是：", getattr(person, "name"))
# 输出：person的地址是： 广东省天河区
print("person的地址是：", getattr(person, "address"))
# 输出：<bound method Person.sayHello of <__main__.Person object at 0x00000283985E7C70>>
print("person的say属性：", getattr(person, "sayHello"))

# 若该属性不存在，则输出默认值
# person的school位于： 不知道什么学校
print("person的school位于：", getattr(person, "school", "不知道什么学校"))


# ==============================================================
#                   setattr函数
#  语法格式：def setattr(__obj: object, __name: str, __value: Any)
#
# ==============================================================

# 给person对象重新设置新的属性
print("reset a new attribute --------------------")

# name
setattr(person, "name", "Topson")
print("new name: ", getattr(person, "name"))        # new name:  Topson

setattr(person, "address", "北京市顺义区")
print("new address: ", getattr(person, "address"))  # new address:  北京市顺义区

# 若属性不存在，则可以给其添加一个新的属性
setattr(person, "weight", 70)
# person's weight value:  70
print("person's weight value: ", getattr(person, "weight"))


# 也可以为该类添加一个新的方法
def say(self):
    print("python 在唱歌")


setattr(person, "person_say", say)
person.person_say(person)                   # python 在唱歌
