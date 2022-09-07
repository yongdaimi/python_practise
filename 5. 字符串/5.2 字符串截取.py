# 截取单个字符
url = "http://www.baid.com"
print(url[10])
print(url[-6])


# 截取多个字符
url = "http://www.baidu.com/"
print(url[7:20])  
print(url[7:-1])
print(url[7:20:1]) # 隔1个步长取一个字符

# 省略start, end, step 参数
print(url[7:])
print(url[-4:])
print(url[:20])
print(url[::2])


