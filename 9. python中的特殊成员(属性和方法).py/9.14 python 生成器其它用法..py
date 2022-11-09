# 本节演示生成器(生成器函数)的其它用法 

# ===================================================================
#                           close() 方法
# send()方法可以携带一个参数，也可以不携带参数，不带参数的话作用与next()
# 方法作用一致，带参数的话则会将参数的值作为yield语句返回值赋值给接收者
# ===================================================================


# 例一：演示生成器send()方法的使用

def foo():
    bar_a = yield "hello"
    bar_b = yield bar_a
    yield bar_b

f = foo()
print(f.send(None))                 # 输出: hello, 程序暂停执行，bar_a 未赋值
print(f.send("PSG.LGD"))            # 输出：PSG.LGD，send() 里的参数会被赋值给当前yield语句的接收者：即bar_a, 所以此时返回 PSG.LGD，但bar_b未赋值
print(f.send("Tundra"))             # 输出：Tundra, 此时send()函数里面的参数被赋值给下一个yield语句的接收者，即bar_b, 所以此时输出Tundra



# ===================================================================
#                           close() 方法
# 程序遇到yield语句会暂停执行，此时如果调用close()方法，会阻止生成器函数
# 继续执行, 并且会在停止执行的位置抛出 GeneratorExit 异常
# ===================================================================

def foo():
    try:
        yield "OG"
    except GeneratorExit:
        print("生成器已退出")
        # yield "Liquid"        # Error! 生成器退出之后，不能再执行 yield语句

f = foo()
print(f.send(None))             # 输出OG，暂停执行
f.close()                       # 生成器已退出

# f.__next__()                    # 生成器退出之后，不能再调用__next__()方法，会报StopIteration异常


print("----------------------------")

# ===================================================================================
#                           throw() 方法
# throw()方法的功能是如果生成器暂停的时候抛出一个异常，则生成器会继续执行，
# 直到遇到下一个yield语句，如果没有下一个yield语句，则会报 方法，会报StopIteration异常
# ===================================================================================


def foo():
    try:
        yield "ame"
    except ValueError:
        print("值错误")
        # yield "maybe"

f = foo()
print(next(f))
f.throw(ValueError)

'''
输出：

ame
Traceback (most recent call last):
  File "d:\python_practise\9. python中的特殊成员(属性和方法).py\9.14 python 生成器其它用法..py", line 62, in <module>
值错误
    f.throw(ValueError)
StopIteration

'''








