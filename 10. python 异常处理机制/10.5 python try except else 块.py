# python 中的异常处理除了 try except 之外，还可以添加 else 块，当 try 里面的代码正确无误
# 不会触发except 里面的异常时，else 块里面的代码也会正常执行，若 try 代码块里面的代码有问题
# 则会触发异常，这样将不会执行else 块里面的代码，示例如下：


try:
    a = 20
    b = int(input("请输入除数："))
    print("输入的除数的值为：", b)
    print("%d / %d = %d" %(a, b, a/b))

except Exception as e:
    print(repr(e))

else:
    print("程序没有异常")

print("程序正常执行")

'''
测试：若输入的除数是 5, 则输出： 【注意：此时会执行 else 代码中的code, 即：“程序没有异常”的提示可以输出】

请输入除数：5
输入的除数的值为： 5
20 / 5 = 4
程序没有异常
程序正常执行
请按任意键继续. . .

测试：若输入的除数是 0，则输出： 【注意：此时不会执行else代码块中的code, 即"程序没有异常"的提示不会输出】

请输入除数：0
输入的除数的值为： 0
ZeroDivisionError('division by zero')
程序正常执行
请按任意键继续. . .


'''