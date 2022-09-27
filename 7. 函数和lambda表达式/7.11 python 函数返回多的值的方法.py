# 和其它编程语言类似，python一次也只能返回一个值，但是python函数可以返回列表和元组，将要返回的多个值保存在序列中，从而间接实现返回多个参数值的目的


# 有两种方式

# 1. 将返回值存储到列表或元组中，然后将这个列表或元组返回；
def return_list():
    add = ["http://www.baidu.com",
     "http://www.taobao.com",
      "http://www.qq.com"]
    return add

print("return_list: ", return_list())


# 2. 函数直接返回多个值，多个值之间用,号进行分隔，python会自动将多个值封装到一个元组中，其返回值仍然是一个元组
def return_tuple():
    return "1", "2", "3"

print("return_tuple: ", return_tuple())


# 3. 可以使用多个变量来接收列表中的多个值

baidu, taobao, qq = return_list()

print("baidu.com: ", baidu)
print("taobao.com: ", taobao)
print("qq.com: ", qq)