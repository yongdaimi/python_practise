# 演示python 自定义迭代器的用法
# 什么是迭代器？像列表、元组、字典、集合这些容器本身就支持使用for循环遍历的，可迭代的容器，就可称为是迭代器

# 一个类要想成为迭代器，必须实现如下两个方法：
# - __next__(self) 方法，返回容器中的下一个元素
# - __iter__(self) 方法，该方法返回一个迭代器

# 使用iter() 函数也可以创建一个迭代器

class listDemo:
    def __init__(self) -> None:
        self.__date = []
        self.__step = 0

    def __next__(self):
        if self.__step <= 0:
            raise StopIteration
        self.__step -=1
        # 返回下一个元素
        return self.__date[self.__step]

    def __iter__(self):
        # 实例对象本身就是迭代器对象，因此可以直接返回self
        return self

    def __setitem__(self, key, value):
        self.__date.insert(key, value)
        self.__step += 1

mylist = listDemo()
mylist[0] = 1
mylist[1] = 2

for i in mylist:
    print(i)

print("================================================")

#-------------------------------------------------------
# 使用iter() 函数创建一个迭代器

my_iter = iter([1, 2, 3, 7, 9])

# 返回迭代器中的下一个对象
print(my_iter.__next__())   # 1
print(my_iter.__next__())   # 2
print(my_iter.__next__())   # 3
print(my_iter.__next__())   # 7
print(my_iter.__next__())   # 9
print(my_iter.__next__())   # 当迭代完迭代器中的所有元素后，如果继续迭代，由会抛出异常



