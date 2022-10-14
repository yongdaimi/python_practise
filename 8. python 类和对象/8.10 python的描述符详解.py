# 演示python 数据描述符的用法

# 一句话概括数据描述符的作用：可以自定义类属性被调用时所做的操作

# 当一个类中的某个属性有数据描述符时，那么每次查找该类的这个属性时，都会调用该类的__get()__方法， 并返回它的值；
# 同样，每次为该的这个属性赋值时， 也会调用__set()__方法；
# 除了使用数据描述符来自定义类属性被调用时的操作以外，还可以使用 property() 或 @property 装饰器


# 数据描述符语法：
# __set__(self, obj, type=None)：在设置属性时将调用这一方法（本节后续用 setter 表示）；
# __get__(self, obj, value)：在读取属性时将调用这一方法（本节后续用 getter 表示）；
# __delete__(self, obj)：对属性调用 del 时将调用这一方法。


class RevealAccess:
    def __init__(self, initval = None, name = 'var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print("getter()", self.name)
        return self.val

    def __set__(self, obj, val):
        print("setter()", self.name)
        self.val = val


class MyClass:
    x = RevealAccess(10, 'var "x"')
    y = 5

m = MyClass()                   
print(m.x)                          # 由于调用了m.x, 相当于调用了getter方法，会输出：getter() var "x"
                                    # 打印出10


m.x = 20                            # 由于有给x属性赋值，相当于调用x的setter方法，会输出：setter() var "x"                  
print(m.x)                          # m.x 相当于又调用了次getter方法，会输出：getter() var "x"
print(m.y)                          # 最终输出两个print 打印的结果：20， 5