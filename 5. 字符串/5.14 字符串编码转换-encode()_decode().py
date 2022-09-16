# python3 默认采用UTF-8的编码方式，英文字符占用1个字节，中文字符占用3个字节

# 将字符串转换为byte类型
result = "百度在线网络".encode()
print(type(result)) # 输出：<class 'bytes'>
print(result) #输出： b'\xe7\x99\xbe\xe5\xba\xa6\xe5\x9c\xa8\xe7\xba\xbf\xe7\xbd\x91\xe7\xbb\x9c'


# 将字符串转换成指定编码的bytes类型
result = "百度在线网络".encode("GBK")
print(result) #输出： b'\xb0\xd9\xb6\xc8\xd4\xda\xcf\xdf\xcd\xf8\xc2\xe7', GBK编码的中文字符占用2个字节

result = "百度在线网络".encode(encoding="GB2312") # 当只有一个参数时，可以省略前面的 encoding=
print(result) #输出：b'\xb0\xd9\xb6\xc8\xd4\xda\xcf\xdf\xcd\xf8\xc2\xe7'


# 将byte类型解码为str类型
origin = "国际邀请赛".encode()
str = origin.decode()
print(str) # 输出：国际邀请赛


# 若使用指定的类型编码，就必须使用指定的类型解码
origin = "国际邀请赛".encode("GBK")
str = origin.decode()
print(str) # 输出异常：'utf-8' codec can't decode byte 0xb9 in position 0: invalid start byte





