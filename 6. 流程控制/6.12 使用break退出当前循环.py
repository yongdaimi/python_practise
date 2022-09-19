url = "http://www.baidu.com"

# 遍历当前URL，如果发现字符p就退出当前循环
for c in url:
    if c == 'p':
        break;
    print(c, end=" ") # 输出 h t t 
else:
    print("我已执行完毕")

print("\n")



# 使用break退出后也不会执行else里面的语句
for c in url:
    if c == 'd':
        break;
    print(c, end=' ')
else:
    print("函数执行完毕") # 输出：h t t p : / / w w w . b a i 

print("\n")


# break 只会退出关联的循环，不会退出所有循环
for i in range(9):
    for j in range(10):
        if j == 2:
            break;
        print("i = ",i, "j = ",j, end="\n")
else:
    print("所有函数执行完毕")
