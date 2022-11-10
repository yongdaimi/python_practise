# 可以使用raise 关键字来抛出异常

# 例一：当除数不是0时，抛出ValueError 异常

try:
    a = int(input("请输入一个大于0的整数："))
    print("当前输入的数是：", a)

    if a == 0:
        raise ValueError("不能输入0")
    else:
        print("20 / %d = %d" %(a, 20/a))
except ValueError as e:
    print(repr(e))

'''
输出结果：

- 测试输入10：

请输入一个大于0的整数：10
当前输入的数是： 10
20 / 10 = 2
请按任意键继续. . .

- 测试输入0：

请输入一个大于0的整数：0
当前输入的数是： 0
ValueError('不能输入0')
请按任意键继续. . .

'''


# 例二：raise 后面也可以什么都不跟，默认抛出RunTimeException
try:
    a = input("请输入一个数字：")
    print("输入的内容是：", a)
    if (not a.isdigit()):
        raise

except RuntimeError as e:
    print(repr(e))

'''
输出：

请输入一个数字：nimasile
输入的内容是： nimasile
RuntimeError('No active exception to reraise')
请按任意键继续. . .

'''

# 例三：若 raise 后什么都不跟，则输出RuntimeException

# raise

'''
Exception has occurred: RuntimeErro
'''