# python 的文件名允许以数字开头，如：123abc.py, 但python的import 语句不允许导入的模块以数字开头；
# 另外，python 的文件名允许含有空格, 如：123 abc.py, 但python的import语句不允许导入的模块名中包含有空格

# 解决方案，使用__import__() 函数进行导入，这里以导入 123 abc.py 模块中的代码为例：

__import__("123 abc") # 会输出：Current module name:  123 abc.py

