# python2 中的super()的用法大致与python3 相同，区别在于，python2不能使用零参数的格式
# 必须至少提供一个参数

# python2 类的定义：

class Person(object):
    pass

class Son(Person):
    pass

'''
简单的说，就是类一定要继承于某个对象，父类没有继承关系时，将默认继承于object对象，object必须写
'''


# python3 类的定义
class Person:
    pass

class Son(Person):
    pass

'''
类似于这样，python3 中可以不写继承于object类，即：默认就是继承于object类
'''


