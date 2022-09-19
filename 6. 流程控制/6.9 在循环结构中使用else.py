# else 语句块会在循环语句执行结束后去执行

# 在while循环执行结束后执行...
url = "http://www.baidu.com"
i = 0
while i < len(url):
    print(url[i], end=" ")
    i += 1
else:
    print("执行了else语句") # 输出：h t t p : / / w w w . b a i d u . c o m 执行了else语句


# 在for循环执行结束后执行...
url = "http://www.taobao.com"
for i in url:
    print(i, end=" ")
else:
    print("for循环执行结束") # 输出：h t t p : / / w w w . t a o b a o . c o m for循环执行结束



