# python 类的定义要点：
# 1. 类的成员变量和成员方法要保持一样的缩进(一般是四个空格)；
# 2. 类的说明文档要放到类头之后，类体之前的位置，这个跟函数的说明文档一样；

class School:
    '''
    这是一个名为School的类
    '''

    address = "GuangDong, GuangZhou"
    totolNum = 2000

    def name(self):
        print("广州中学")

    def master(self):
        print("校长是张三")


help(School)

'''
输出：
class School(builtins.object)
 |  这是一个名为School的类
 |  
 |  Methods defined here:
 |  
 |  master(self)
 |  
 |  name(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  address = 'GuangDong, GuangZhou'
 |  
 |  totolNum = 2000

'''
