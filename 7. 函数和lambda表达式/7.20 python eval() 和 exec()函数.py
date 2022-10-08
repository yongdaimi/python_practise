# exec() 和 eval() 函数均可用于执行一段指定的代码， 区别是exec()函数执行的代码可以没有返回值，eval() 函数执行的代码
# 必须要有返回值

# 例1： 给a 赋值
a = 4
exec("a = 10")
print("a = ", a) # 输出 a = 10

# 例2：计算1+2+3的和
a = 1
b = 2
c = 3
d = eval("a + b + c")
print("d = ", d) # 输出 在= 6

# 例3：限定exec() 执行时的作用域
list1 = {'a':10, 'b':20}
exec("c = a + b; print(c)", list1) # 输出30
