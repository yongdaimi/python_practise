# __rept__() 可以自定义类的输出格式，类似于java 中的toStirng()方法，

# 例：一般而言，输出python对象的时候，输出的结果都是一个 对象地址的形式：

class Person:
    name = "zhangsan"
    address = "广东省广州市"

    def say(self):
        print("在说话")

person = Person()
print(person)                       # 输出：<__main__.Person object at 0x0000026B6E2B6DA0>
print("----------------------------------------------")

# 对上述示例进行改造，使之能输出类的详细信息

class Person:
    name = "zhangsan"
    address = "广东省广州市"

    def say(self):
        print("在说话")

    def __repr__(self) -> str:
        return "当前person的名称是："+ Person.name +", 地址是："+ Person.address

person = Person()
print(person)                      # 输出：当前person的名称是：zhangsan, 地址是：广东省广州市


