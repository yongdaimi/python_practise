# 演示如何处理pythton程序中的异常


try:
    b = 5
    c = 5 / 0
    print("c: ", c)
except ZeroDivisionError:
    print("除数不能为零")

'''
上述code有添加 try ... except, 若不添加此异常处理，则会抛出：

Traceback (most recent call last):
  File "d:\python_practise\10. python 异常处理机制\10.1 python常见异常处理类型.py", line 4, in <module>
    c = 5 / 0
ZeroDivisionError: division by zero

'''