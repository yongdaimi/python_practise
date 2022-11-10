# 之前介绍的else 关键字 必须和 try except 搭配使用，但是 finally 主键字只需要和 try 块搭配使用即可，finally块中的
# 代码不管有没有异常都会得到执行

try:
    a = 20
    b = int(input("请输入除数："))
    print("输入的除数的值为：", b)
    print("%d / %d = %d" %(a, b, a/b))

except Exception as e:
    print(repr(e))
finally:
    print("执行到了finally语块处")

'''
输出：

- 假设输入的值是 5:

请输入除数：5
输入的除数的值为： 5
20 / 5 = 4
执行到了finally语块处
请按任意键继续. . .

- 假设输入的值是 0:

请输入除数：0
输入的除数的值为： 0
ZeroDivisionError('division by zero')
执行到了finally语块处
请按任意键继续. . .

可以看到，不管代码有没有异常，最终都会执行finally语法块中的代码
'''
