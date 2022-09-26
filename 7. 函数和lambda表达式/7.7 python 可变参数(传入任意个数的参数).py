# python 定义可变参数有两种形式

'''
结论：
重要：
调用函数时，
非关键字的参数会存储到元组参数(*args)中, 这里的非关键字参数指的是print(a, b, c) a, b, c这种的没有指明默认值的参数；
关键字参数则会存储到字典参数(**args)中， 这里的关键字参数指的是print(a = '20', b = '16', c= '27', 这种有指明默认的值的参数)；
'''


# 形式一： 使用 *arg, 当作为*arg传入时，系统会将其当做是一个元组

from dis import dis


def dis_str(home, *arg):
    print("home: ", home)
    print("*arg 的类型是：", type(arg), "内容是: ", arg)
    for s in arg:
        print(s)

# 传入任意多的参数
dis_str("OG", "ana", "topson", "ceb", "jerax", "notail")

'''
输出：

*arg 的类型是： <class 'tuple'> 内容是:  ('ana', 'topson', 'ceb', 'jerax', 'notail')
ana
topson
ceb
jerax
notail

'''


# 形式二： 使用 *arg, 当作为**arg传入时，系统会将其当做是一个字典, 需要注意，后面的字典在书写时，需要写成 key = value的形式，比如a = '1',
#         不能写成 a : '1'
print("---------------------------------------------------")
def dis_str(home, *str, **course):
    print(home)
    print(str)
    print(course)
    print("**course type is: ", type(course))

dis_str("OG","Screct","PSG.LGD","NewBee", a = '1', b = '2', c = '3')

my_dict = {1:2, 2:3, 3:4, 5:5}
print(my_dict)







