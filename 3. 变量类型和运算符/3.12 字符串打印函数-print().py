# print() 函数不仅可以输出一个变量，还可以输出多个变量，并且还有其它功能。
'''
语法格式：
print (value,...,sep='',end='\n',file=sys.stdout,flush=False)

- value,.. 代表可以输出多个变量和值；
- sep, 用于指定多个值之前的分割符，默认是空字符
- end, 用于指定末尾是否添加换行符, 默认是\n, 代表输出完成后会自动换行；
- file,用于指定输出位置，默认为屏幕；
- flush, 用于指定输出完成后是否立即刷新缓冲区

'''

# 输出多个参数的值
from operator import truediv


name = "ZhangSan"
age = 20
print("名称：", name, ",年龄", age) # 输出：名称： ZhangSan ,年龄 20


# 输出的多个参数间使用 - 分割
year = 2022
month = 10
day = 20
print(year, month, day, sep = '-') # 输出：2022-10-20

# 输出完成后不自动换行
name1 = "ZhangSan"
name2 = "Lisi"
name3 = "WangWu"
print(name1, name2, name3, sep=' ', end='') # 输出：ZhangSan Lisi WangWu

# 指定输出位置为D:\\name.txt
out_file = open("D:\\name.txt", "w")
name1 = "Topson"
name2 = "ANA"
print(name1, name2, sep=' ', file = out_file) # 会自动在D盘根目录下生成name.txt file.
out_file.close()

# 输出时立即刷新缓冲区，不建议设置为true, 会降低性能
print("\n")
year = 2022
month = 10
day = 8
print(year, month, day, sep = '-', flush=True) # 输出：2022-10-8





