flag = False
for i in range(100):
    if (flag == True):
        print("程序将要退出...")
        break;
    if (i == 50):
        flag = True
    print("i = ", i)

print("程序执行完毕")

