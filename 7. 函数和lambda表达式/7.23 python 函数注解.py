# python 中的注解的主要目的是为了： 为函数中的形参或返回值提供类型提示信息

# 例一：
def foo(x:str, y:str="topson")->str:
    pass

print(foo.__annotations__) # 输出：{'x': <class 'str'>, 'y': <class 'str'>, 'return': <class 'str'>}


# 例二：
# def foo2(x:"必须是int类型", y:"必须是字符串类型")->"必须是int类型":
#     print("y: ", y)
#     return y

# print(foo2.__annotations__) # 输出：{'x': '必须是int类型', 'y': '必须是字符串类型', 'return': '必须是int类型'}

'''
注意要点：
1. 注解的用法
    - 对函数参数而言， 就是在函数参数的后面加上冒号(:), 再加上注解名；
    - 对函数返回值而言， 就是在->与：之间写上注解名；
2. 注解可以写成任意类型，如 int, str, 表达式或其它，python 解释器会自动忽略；
3. 给函数添加注解后，可以使用 __annotations__ 属性去获取已添加的注解，它会返回一个字典；
'''


 