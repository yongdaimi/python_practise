# 在函数体内部使用 global 关键字修饰某个局部变量后，该局部变量就会变成全局变量


# =================================================================
#               例一: 在函数体将局部变量转换为全局变量
# =================================================================

ana = "ana"
topson = "topson"
ceb = "ceb"

def print_msg():
    global website
    website = "http://www.baidu.com"
    print("in func: website: ", website)

# 在将局部变量转换为全局变量时，不能会全局变量赋初值，否则会引发语法错误
# def print_msg():
#     global website = "http://www.baidu.com" # 错误：解释器会报：Statements must be separated by newlines or semicolons
#     print("in func: website: ", website)

print_msg()
print("website: ", website)


# ==========================================================================================
#       例二: 使用globals()内置函数获取程序范围内的所有全局变量, 
#       结果将会以字典的形式给出
# ==========================================================================================
print(globals())

'''
输出：

{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001505B334790>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:\\python_practise\\7. 函数和lambda表达式\\7.14 python 变量作用域(局部变量_全局变量).py', '__cached__': None, 'ana': 'ana', 'topson': 'topson', 
'ceb': 'ceb', 'print_msg': <function print_msg at 0x000001505B38A0E0>, 'website': 'http://www.baidu.com'}

'''
#  修改 ana 全局变量的值
globals()['ana'] = "ANA"
print(globals()['ana']) # 输出：ANA


print("-------------------------------------------------")


# =========================================================================================
#                   例三：使用locals()内置函数获取函数内所有局部变量的值
# =========================================================================================
def test_locals():
    a = "ame"
    b = "maybe"
    c = "charles"
    d = "fy"
    e = "xnova"

    print("all local varibles: ", locals())

test_locals()

'''
输出：

all local varibles:  {'a': 'ame', 'b': 'maybe', 'c': 'charles', 'd': 'fy', 'e': 'xnova'}

'''

print("-------------------------------------------------")

# 外部调用locals()函数, 在外部调用 locals() 函数时，其作用与globals() 函数等同
print(locals())

'''
输出：
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000026342FC4790>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:\\python_practise\\7. 函数和lambda表达式\\7.14 python 变量作用域(局部变量_全局变量).py', '__cached__': None, 'ana': 'ana', 'topson': 'topson', 'ceb': 'ceb', 
'print_msg': <function print_msg at 0x000002634301A170>, 'website': 'http://www.baidu.com', 'test_locals': <function test_locals at 0x000002634301A200>}

'''

#  locals() 函数在函数内部时，无法像globals()函数那样，修改变量的值
def test_locals_func():
    a = 10
    b = 20
    print(locals())
    locals()['a'] = 40
    print("after modify a: ", a)

test_locals_func() # 输出：{'a': 10, 'b': 20} after modify a:  10



print("--------------------------------------------------------")
# =========================================================================================
#                   例四：var(object) 可以返回指定对象范围内所有变量组成的字典
# =========================================================================================

name = "百度"
website = "http://www.baidu.com"

class Demo:
    name1 = "网易"
    website1 = "http://www.163.com"

print("有object:")
print(vars(Demo))

print("无object:") # 作用与locals() 等同
print(vars())







