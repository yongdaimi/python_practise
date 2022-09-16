# 1. 判断是否符合条件
# age = int(input("请输入你的年龄："))
# print("输入的年龄是：%d" %age)

# if age < 18 :
#     print("你还未成年")
#     print("如果你已经得到同意，请忽略上述提示")
# print("正在使用中...")  


# 2. 不符合条件时退出
# import sys


# age = int(input("请输入你的年龄："))

# if age < 18 :
#     print("你还未成年")
# else:
#     print("你已经成年")
#     sys.exit()

# print("program is running...")


# 3. 判断某人的身材是否合理
# height = float(input("请输入您的身高："))
# weight = float(input("请输入您的体重："))

# # 计算BMI指数
# bmi = weight / (height * height)

# if bmi < 18.5:
#     print("BMI指数为："+str(bmi))
#     print("体重过轻")
# elif bmi >= 18.5 and bmi < 24.9:
#     print("BMI指数为："+str(bmi))
#     print("正常范围，继续保持")
# elif bmi >= 24.9 and bmi <29.9:
#     print("BMI指数为："+str(bmi))
#     print("体重过重")
# else:
#     print("BMI指数为："+str(bmi))
#     print("肥胖")


# 4. 判断表达式是否成立
b = False
if b:
    print("b is True")
else:
    print("b is False")

n = 0
if n:
    print("n 不是零值")
else:
    print("n 是零值")

s = ""
if s:
    print("s 不是空字符串")
else:
    print("s 是空字符串")

l = []
if l:
    print("l 不是空列表")
else:
    print("l 是空列表")

d = {}
if d:
    print("d 不是空字典")
else:
    print("d 是空字典")

def func():
    print("func()函数被调用")

if func():
    print("func()函数的返回值不为空")
else:
    print("func()函数的返回值为空")

# 对于没有return返回值的函数，返回值为空，也即：None.