# python zip() 函数可以将序列（列表、元组、字典、集合、字符串中对应元素的位置重新组合，以生成一个新的元组

# 演示：将下列序列中的每个元素进行组合，以生成一个元组

my_list = [1, 2, 3, 4, 5]
my_tuple = (21, 22, 23, 24, 25)

print([x for x in zip(my_list, my_tuple)]) # 输出：[(1, 21), (2, 22), (3, 23), (4, 24), (5, 25)]

my_dict = {31:2, 32:4, 33:5}
my_set = {41, 42, 43, 44}
print([x for x in zip(my_dict, my_set)]) # 输出：[(31, 41), (32, 42), (33, 43)], 注意：由于字典里面只包含3个元素，而集合里面包含4个元素，
# 因此无法与集合中的第4个元素配对，所以只会输出3组


my_char1 = "zhangsanfeng"
my_char2 = "lishimin"

print("my_char1的长度是：", len(my_char1))
print("my_char2的长度是：", len(my_char2))
print([x for x in zip(my_char1, my_char2)]) # 输出：[('z', 'l'), ('h', 'i'), ('a', 's'), ('n', 'h'), ('g', 'i'), ('s', 'm'), ('a', 'i'), ('n', 'n')]

'''
结论：
当序列中的元素个数不一致时，会取最短的序列为准进行压缩
'''

# 对于zip()函数返回的zip对象，既可以像上面程序那样，通过遍历提取其存储的元组，也可以像下面的程序这样，通过调用list()函数将zip()对象强制转换成列表：
my_list = [1, 2, 3, 4, 5]
my_tuple = (9, 8, 7, 6, 5)

print(list(zip(my_list, my_tuple)))




