# python 关键字参数的意思就是说在调用python函数的时候可以手动指定函数参数的值

# 例： 可以在调用参数时将arg2 参数放置到前面

def print_value(arg1, arg2):
    print("arg1: ", arg1)
    print(">>>>>>>>>>>>>>>>> ", arg2, " <<<<<<<<<<<<<<<<")

print_value(arg2="http://www.baidu.com", arg1="ojbk")