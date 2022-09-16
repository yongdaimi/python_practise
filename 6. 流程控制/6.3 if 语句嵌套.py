# if else 之前还可以继续嵌套if else

age = int(input("请输入您的年龄："))

if age < 12:
    print("你应该念小学")
else:
    if age >= 12 and age < 15:
        print("你应该念初中")
    elif age >= 15 and age < 18:
        print("你应该念高中")
    elif age >= 18 and age < 21:
        print("你应该念大学")
    else:
        print("你大学毕业了，该结婚了");

print("程序运行结束")