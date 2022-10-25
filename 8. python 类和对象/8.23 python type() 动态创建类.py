# type() 的用法
# - 查看当前数据或对象的类型；
# - 动态创建新类, 语法格式：
# - type(name, bases, dict), 
#       name 代表新创建的类型的名称，
#       bases是一个元组，用于存储该元素的父类，注意：若只有一个父类时，末尾也需要用逗号，如(object, )
#       dict是一个字典，用于表示类中定义的属性或方法


# 例一： 查看当前对象的类型
class Dog:
    pass

dog = Dog()
print("dog type: ", type(dog))      # 输出：dog type:  <class '__main__.Dog'>

# 例二：动态创建一个新类, 名为：Person

def say(self):
    print("在说话")

Person = type("Person", (object,), dict(say = say, name = "zhangsan"))

# 创建一个Person对象
person = Person()
# 调用say() 方法和 name 属性
person.say()                                    # 在说话
print("current person name: ", person.name)     # current person name:  zhangsan
print("---------------------------------------")

# 例三: 动态创建一个新类，名为Student

def go_school(self):
    print("去学校上学")

Student = type("Student", (object,), dict(go_school = go_school, name = "xiaohua"))

stu = Student()
stu.go_school()                                 # 去上学
print("student's name is: ", stu.name)          # student's name is:  xiaohua