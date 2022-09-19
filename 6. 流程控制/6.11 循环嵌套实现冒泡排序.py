# 利用for循环实现用冒泡排序算法对[5, 8, 4, 1] 进行排序
data = [5, 8, 4, 1]
for i in range(len(data) - 1):
    for j in range(len(data) - i -1):
        if(data[j]>data[j+1]):
            data[j],data[j+1] = data[j+1],data[j]

print("排序后：", data) # 输出：排序后： [1, 4, 5, 8]