# 逆序函数reversed()可以对序列中的元素进行逆序排序

print([x for x in reversed([1, 2, 3, 4, 5])]) # 输出 [5, 4, 3, 2, 1]

print([x for x in reversed((1, 2, 3, 4, 5))]) # 输出 [5, 4, 3, 2, 1]

print([x for x in reversed("zhangsanfeng")]) # ['g', 'n', 'e', 'f', 'n', 'a', 's', 'g', 'n', 'a', 'h', 'z'] 不懂为什么会输出这个

print([x for x in reversed(range(10))]) # 输出：[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# 不使用列表推导式，使用list()函数进行输出
print(list(reversed(range(10)))) # 输出：[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 执行逆序操作生成新的列表时，并不会改变原有的列表
a = [1, 2, 3, 4, 5]
b = list(reversed(a))

print(a)        # 输出：[1, 2, 3, 4, 5]
print(b)        # 输出：[5, 4, 3, 2, 1]

