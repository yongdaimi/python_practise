# python 中的property()函数也可以用来实现自定义属性访问的操作
# but.... 这个东西有什么用呢？

class Student:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        print("调用了getter()方法")
        return self.__name

    def set_name(self, name):
        print("调用了setter()方法, 新set的名称是：", name)
        self.__name = name

    def clear_name(self, name):
        print("调用了clear()方法")
        self.__name = ""

    name = property(get_name, set_name, clear_name, "Student类的name属性")
    
help(Student.name)
print("doc: ", Student.name.__doc__)


student = Student("Mira")
print("student.name: ", student.name)

# 设置新名称
student.name = "Collapse"

print("student的新名称: ", student.name)

'''
输出：

Help on property:

    Student类的name属性

调用了getter()方法
student.name:  Mira
调用了setter()方法, 新set的名称是： Collapse
调用了getter()方法
student的新名称:  Collapse

'''