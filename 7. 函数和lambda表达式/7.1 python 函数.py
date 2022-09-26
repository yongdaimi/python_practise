# 演示python 函数的用法

def my_len(str):
    length = 0
    for c in str:
        length = length + 1
    return length


len1 = my_len("http://www.baidu.com")
len2 = my_len("http://www.qq.com")

print(len1)
print(len2)


# python 函数的说明文档位于函数内部，所有代码的最前面

def print_name():
    '''
    打印一个名称
    '''
    print("print_name()_ZhangSan")

print_name()

help(print_name)
print(print_name.__doc__)

help(print)


