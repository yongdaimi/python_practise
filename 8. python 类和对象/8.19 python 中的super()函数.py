# python 中的super()函数

# 例一：子类中若没有写构造方法，将会调用父类中的构造方法

class Person:
    def __init__(self, name) -> None:
        print("Person中的构造方法，__init__(self, name)")
        self.name = name


class Son(Person):
    pass

son = Son("Qualcomm")

print("--------------------------------------------------------------")

# 例二：若子类同时继承了多个父类，默认将会调用第一个直接父类的构造方法
class Person:
    def __init__(self, name) -> None:
        self.name = name

    def say(self):
        print("我是%s, 我会说话" %self.name)


class Animal:
    def __init__(self, food) -> None:
        self.food = food

    def eat(self):
        print("我在吃东西，东西是：", self.food)


class Girl(Person, Animal):
    pass

girl = Girl("xiaohua")
girl.say()                      # 输出：我是xiaohua, 我会说话，注意：只调用了Person类的构造方法
# girl.eat()                    # 会报错：提示：'Girl' object has no attribute 'food'， 即找不到food这个属性，因为没有调用Animal中的构造方法

print("--------------------------------------------------------------")


# 例三：对例二进行改造，使之能够调用Person类和Animal类中的构造方法

class Person:
    def __init__(self, name) -> None:
        self.name = name

    def say(self):
        print("我是%s, 我会说话" %self.name)


class Animal:
    def __init__(self, food) -> None:
        self.food = food

    def eat(self):
        print("我在吃东西，东西是：", self.food)


class Girl(Person, Animal):
    def __init__(self, name, food) -> None:
        super().__init__(name)                  # super() 函数将只会调用第一个直接父类的构造方法, 也就是说只会调用Person类的构造方法
        Animal.__init__(self, food)             # 调用其它父类的构造方法，需要手动为self传值

girl = Girl("xiaohua", "apple")
girl.say()                      # 输出：我是xiaohua, 我会说话，注意：只调用了Person类的构造方法
girl.eat()                      # 输出：我在吃东西，东西是： apple
