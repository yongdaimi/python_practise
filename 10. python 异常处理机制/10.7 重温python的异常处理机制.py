# 1. python 中的finally块在任何条件下均会执行，比如 break, return ...
# 但如果你是使用系统的强制退出方法退出了程序，则finally 块也不会执行


# 例一：代码在执行到某个条件时 return, finally 块仍然会执行

try:
    for i in range(10):
        if i == 5:
            break
        else:
            print("i = %d" %(i))

finally:
    print("程序执行到finally语块处")

'''
输出：

i = 0
i = 1
i = 2
i = 3
i = 4
程序执行到finally语块处
'''

# 例二：不要在 finally 语块中使用 return 语句，因为它会干扰到 try 块中的return 语句：

def foo():
    try:
        return True

    finally:
        return False

print(foo())
'''
输出: 本应输出 True: 结果输出 False
'''


# 例三：当使用系统的退出语句时，finally 语块将不会被执行

import os

try:
    for i in range(10):
        if i == 5:
            os._exit(0)
        else:
            print("i = %d" %(i))

finally:
    print("程序执行到finally语块处")

'''
输出：
i = 0
i = 1
i = 2
i = 3
i = 4


因为使用系统的强制退出函数，所以没有执行 finally 语块中的代码
'''



