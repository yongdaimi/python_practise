# 如何想办法访问到python中的私有类属性或方法

# 事实上python 只是对以__打头的成员或方法做了重命名，让其没有办法使用正常的 对象.方法名()访问
# python会把成员或方法重命名为：_类名__方法名() 或_类名__属性名 这种形式
# 即以一个下划线打头类名，两个下划线打头方法名。

# 例：

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


person = Person()
person.name = "ana"
person.address = "广东省厦门市"

# 直接调用私有方法会报错：AttributeError: 'Person' object has no attribute '__print_info'
# person.__print_info()

# 换种方式调用：
person._Person__print_info() # 输出：当前person的详细信息为：name: ana, address: 广东省厦门市


# 尝试修改私有属性
person._Person__name = "bigdaddy_notail"
person._Person__address = "福建省福州市"
person._Person__print_info()    # 输出：当前person的详细信息为：name: bigdaddy_notail, address: 福建省福州市

'''

从上述输出可以看到，当使用_类名__方法名或属性名调用时，不仅能够访问到私有的属性或方法，还可以绕过getter()方法和setter()方法
的访问限制

'''