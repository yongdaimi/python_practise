# 演示python多态的用法

# 例一：

class Person:
    def info(self):
        print("我是Person")

class Man(Person):
    def info(self):
        print("我是Man")

class Woman(Person):
    def info(self):
        print("我是Woman")

a = Person()
a.info()

a = Man()
a.info()

a = Woman()
a.info()

print("-------------------------------------")

# 例二： 对上面的例子进行改写

class Person:
    def __init__(self, name) -> None:
        self.name = name
        pass

    def info(self, person):
        person.info()

class Man(Person):
    def info(self):
        print("我叫%s, 我是%s" %(self.name, "Man"))

class Woman(Person):
    def info(self):
        print("我叫%s, 我是%s" %(self.name, "Woman"))

person = Person("person 基类")
person.info(Man("SunGokong"))                   # 我叫SunGokong, 我是Man
person.info(Woman("Bulma"))                     # 我叫Bulma, 我是Woman


# 例三：扩展

def call_func(func, a , b):
    func(a , b)

def add(a, b):
    print("a + b = %d" %(a+b))

def cheng(a, b):
    print("a * b = %d" %(a*b))

call_func(add, 2, 3)                            # a + b = 5
call_func(cheng, 4, 5)                          # a * b = 20
