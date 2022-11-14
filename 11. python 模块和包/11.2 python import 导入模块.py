# 演示下python improt 的方式导入模块 和 使用 from ... import 的方式导入模块

import sys

print(sys.argv[0])                  # sys 模块下的argv变量用于获取运行python程序的命令行参数，其中argv[0]用于获取当前python程序的存储路径


from os import sep

print(sep)                          # sep 变量代表指定平台的分隔符


'''
输出：

d:\python_practise\11. python 模块和包\11.2 python import 导入模块.py
\
'''

