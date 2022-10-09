# 演示python 面向对象

class Person:
    name = "Zhangsan"
    age = 20
    sex = 1

    def say(self):
        print("说话")

    def run(self):
        print("跑")

    def skip(self):
        print("跳")


person = Person()
person.say()
person.run()
person.skip()

'''
输出结果：

说话
跑
跳

'''

