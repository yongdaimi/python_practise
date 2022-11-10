# 演示 python 中 __call__() 方法的使用

class Person:

    def __call__(self, name, address):
        print("名字是：%s, 地址是：%s" %(name, address))

    def say(self):
        print("oh my god")

# 该对象已变成可调用对象

person = Person()
person("zhangsan", "广东省天河区")      # 输出：名字是：zhangsan, 地址是：广东省天河区

person.say()                           # 实例方法 say() 也是一个可调用对象


class Son:
    def __init__(self) -> None:
        self.name = "Lisi"
        self.age = 20


    def go_school(self):
        print("去上学")

son = Son()
if (hasattr(son, "name")):
    print(hasattr(son.name, "__call__"))                # 输出：False, name 是实例属性，不是可调用对象

print("------------------------------")

if (hasattr(son, "go_school")):
    print(hasattr(son.go_school, "__call__"))           # 输出：True



