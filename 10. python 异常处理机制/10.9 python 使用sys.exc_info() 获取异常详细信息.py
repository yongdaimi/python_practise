# 本节演示如何使用sys模块下的exc_info()方法获取异常的详细信息，并且使用traceback 模块下的print_tb()方法查看具体的错误信息

# 使用exc_info() 需要导入sys模块，这个方法会返回包含三个元素的元组
# 这三个元素分别为：
# 第一个元素代表 错误的类型
# 每二个元素代表 错误的实例
# 第三个元素是一个 traceback 对象，这个traceback 对象可以使用 traceback 对象的 print_tb() 方法查看

import sys
import traceback

try:
    a = int(input("请输入一个整数:"))
    print("当前输入的值为：", a)
    c = 20 / a
    print("20 / %d = %d" %(a, 20/a))

except:
    print(sys.exc_info()) # 输出的元组内容：(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x000002468C32EEC0>)
    print(traceback.print_tb(sys.exc_info()[2]))

