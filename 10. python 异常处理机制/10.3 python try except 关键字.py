# 本节演示如何处理多个异常的情况

try:
    a = int(input("请输入被除数："))
    b = int(input("请输入除数："))
    print("Tips: 输入的被除数是：%d, 除数是：%d" %(a, b))
    print("%d/%d的商是：%d" %(a, b, a/b))

except (ValueError, ArithmeticError):           # 多个异常之间可以使用小括号进行包裹，中间有逗号进行分隔
    print("程序发生了数字格式异常")

except:
    print("未知异常")

print("程序正常执行")



# 获取特定异常的详细信息

try:
    a = 5
    b = 0
    c = a / b
    print("c = %d", c)

except Exception as e:                          # 如果想输出异常的详细信息，可以使用 as 关键字
    print(e.args)                               # ('division by zero',)
    print(str(e))                               # division by zero ，
    print(repr(e))                              # ZeroDivisionError('division by zero')