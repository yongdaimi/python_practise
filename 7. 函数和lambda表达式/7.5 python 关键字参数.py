# python 关键字参数的意思就是说使用形参的名字来确定输入的参数值，通过此方法指定函数实参时，不需要与形参的位置完全一致，只需要将参数名写对即可。

# 例： 可以在调用参数时将arg2 参数放置到前面

def print_value(arg1, arg2):
    print("arg1: ", arg1)
    print(">>>>>>>>>>>>>>>>> ", arg2, " <<<<<<<<<<<<<<<<")

print_value(arg2="http://www.baidu.com", arg1="ojbk")