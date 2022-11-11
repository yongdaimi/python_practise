# 使用traceback 模块获取和保存异常信息

import traceback

class UnknownException(Exception):
    pass

def first_method():
    second_method()

def second_method():
    thrid_method()

def thrid_method():
    forth_method()

def forth_method():
    raise UnknownException("unknown exception") 

try:
    first_method()

except:
    traceback.print_exc()
    traceback.print_exc(file = open("./trace.txt", "a"))