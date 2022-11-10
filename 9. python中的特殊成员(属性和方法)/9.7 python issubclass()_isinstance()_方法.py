# 演示 issubclass()、isinstance()、__bases__、__subclasses__ 这些方法或属性的使用


# ============================================================
#                       issubclass()
#          判断某个类是否是指定类的子类
# ============================================================

# 例一：判断字符串类型str 是否是 object 类型的子类
print(issubclass(str, object))                  # 输出：True
print(issubclass(list, object))                 # 输出：True

# 也可以用来判断一个类型是否是给定的元组中的类型的子类
# 判断元组类型 tuple 是否是给定元组中 (list, object) 其中一种类型的子类
print(issubclass(tuple, (list, object)))        # 输出：True



# ============================================================
#                       isinstance()
#          判断对象是否是给定类型的实例
# ============================================================

# 例一：判断 name 是否是字符串类型 str 的实例
name = "zhangsan"
print(isinstance(name, str))                    # 输出 True

og = ("ana", "topson", "ceb", "jerax", "notail")
print(isinstance(og, tuple))                    # 输出 True

# 也可以用来判断是否是给定元组中某一个类型的实例
tundra = [1, 2, 3, 4, 5]
print(isinstance(tundra, (list, str)))          # 输出 True



# ============================================================
#                     __bases__
#          通过类的__bases__ 属性可以查看它的所有直接父类
# ============================================================

class A:
    pass

class B:
    pass

class C(A, B):
    pass

class D(A):
    pass

print(C.__bases__)                              # 输出：   (<class '__main__.A'>, <class '__main__.B'>)
print(C.__base__)                               # 输出：<class '__main__.A'>


# ============================================================
#                     __subclasses__()
#          通过类的 __subclasses__  方法可以查看它的所有子类
# ============================================================
print(A.__subclasses__())                       # 输出：[<class '__main__.C'>, <class '__main__.D'>]
