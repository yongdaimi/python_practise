# 偏函数可以对原始函数进行二次封装， 将原始函数的部分参数预先绑定为指定值。
# 使用时需要先导入 functools 模块 (from functools import partial)


from functools import partial

def display(name, age):
    print(name, "的年龄是：", age)

# 例一：
testfunc = partial(display, "Zhangsan")
testfunc(13) # 输出：Zhangsan 的年龄是： 13

# 例二：
testfunc2 = partial(display, age = 20)
testfunc2("liSi") # 输出：liSi 的年龄是： 20

# 综上，偏函数中指定默认参数时，其用法与普通函数中指定默认参数类似


# 例三：
def mod(n, m):
    return n % m

mod_by_100 = partial(mod, 100) # 这里会缺省地将100赋值给n

print(mod(100, 7)) # 输出： 2
print(mod_by_100(7)) # 输出： 2


