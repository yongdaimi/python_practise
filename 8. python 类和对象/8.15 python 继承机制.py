# 演示python 继承机制

class Animal:
    
    def __init__(self) -> None:
        self.name = Animal
    
    def shout(self):
        print("会叫")

    def eat(self):
        print("会吃东西")

    def intro(self):
        print("我是一只动物, 我的名字是：", self.name)

class Pet:
    def __init__(self) -> None:
        self.name = Pet

    def play(self):
        print("还是一个宠物")

    def intro(self):
        print("我是一个宠物, 我的名字是：", self.name)

class Cat(Animal, Pet):
    def zhualaosu(self):
        print("猫眯会抓老鼠")


cat = Cat()
cat.shout()
cat.eat()
cat.zhualaosu()
cat.play()
cat.intro()                     # 输出：我是一只动物, 我的名字是： <class '__main__.Animal'>
                                # Note： 当存在多重继承时，且多重继承中存在着同名的方法时，
                                # 在调用时总是优先调用先写的父类


'''
输出：
会叫
会吃东西
猫眯会抓老鼠
还是一个宠物
'''
