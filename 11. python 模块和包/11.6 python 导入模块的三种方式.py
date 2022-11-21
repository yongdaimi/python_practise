# 这里主要介绍一下，如何引入python 中的第三方模块，一般情况下，我们都是将第三方模块添加到与当前执行模块的同级目录下
# 如果不能放在同级目录下，可以下列三种方式，使当前执行的模块能够找到这个新模块的位置：

# - 建立python 环境变量 PYTHONPATH, 在其中添加第三方模块的位置；
# - 将第三方模块添加到python 安装目录的 lib/site-packages 目录下：
# - 手动给系统内置变量 ssy.path 添加，让系统知道这个第三方模块的位置


# 可以通过 sys.path 查看系统会去哪些位置查找第三方模块

import sys

print(sys.path)

'''
这边输出的是一个列表：

['d:\\python_practise\\11. python 模块和包', 'E:\\sys\\Python\\python310.zip', 'E:\\sys\\Python\\DLLs', 'E:\\sys\\Python\\lib', 'E:\\sys\\Python', 'E:\\sys\\Python\\lib\\site-packages']

'''

# 现在演示一下导入 third_party 目录下cmd.py 模块

sys.path.append('D:\\python_practise\\11. python 模块和包\\third_party')
import my_cmd

my_cmd.cmd_info()           # 会输出：MODULE NAME: cmd


