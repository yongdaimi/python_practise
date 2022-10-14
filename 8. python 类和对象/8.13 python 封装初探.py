# 演示下python中类的封装，封装可以只向外部提供必要的访问接口，屏蔽内部的实现细节

# python 中的访问权限有两种：public, private, 但python本身没有private public 访问修饰符，
# 同时，python约定:
#  1. 凡是以__ (两个下划线)开头的成员或方法均视为类的私有属性或私有方法, 没有以__开头的则视为公共成员或方法；
#  2. 以_ (单下划线)开头的虽然在类名也能够被访问，但仍然将其视为私有属性或方法；
#  3. 以__开头或结尾的方法(如：__init__())视为python内部提供的方法，一般编写函数时尽量不要以此命名。


# 问题一：给类成员加上proerty()函数访问限制后，那这个类成员到底算做是类属性还是实例属性？


class Person:

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) > 5:
            raise ValueError("name's length must be less than 5 !")
        else:
            self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        if address.startswith("广东省"):
            self.__address = address
        else:
            raise ValueError("address must be start with 广东省")
            
    # 为 name 属性绑定 getter() 方法和 setter() 方法
    name = property(get_name, set_name)

     # 为 address 属性绑定 getter() 方法和 setter() 方法
    address = property(get_address, set_address)

    def __print_info(self):
        print("当前person的详细信息为：name: %s, address: %s" %(self.__name, self.__address))


print("Person.name: ", Person.name)             # Person.name:  <property object at 0x000001C49CE736F0>
print("Person.address: ", Person.address)       # Person.address:  <property object at 0x000001C49CE73650>

person = Person()

# 修改person 对象的名称和地址
print("------------------------ 修改person对象的名称和地址 -------------------------")
person.name = "lisi"
person.address = "广东省厦门市"

# Error! name's length must be less than 5 !
# person.name = "zhangsan"

# Error! ValueError: address must be start with 广东省
# person.address = "福建省福州市"

# 不允许调用私有的方法
# Error! AttributeError: 'Person' object has no attribute '__print_info'
# person.__print_info()

print("Person info: name: %s, address: %s" %(person.name, person.address))

'''
输出：

Person info: name: 佚名, address: 广东省广州市
------------------------ 修改person对象的名称和地址 -------------------------
Person info: name: lisi, address: 广东省厦门市


'''



        
    