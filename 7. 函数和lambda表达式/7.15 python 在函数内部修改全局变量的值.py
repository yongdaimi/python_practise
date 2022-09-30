# python 在函数内部不能直接修改全局变量的值


name = "网易"

# def test():
#     print("name: ", name)
#     name = "百度"           # 输出错误：local variable 'name' referenced before assignment

# 若要修改，有以下两种解法：

# 解法一：直接使用globals() 修改
def test():
    print("name", globals()['name'])
    globals()['name'] = "百度"
    name = "腾讯"

test()                                          # 输出：网易
print("outer name: ", name)                     # 输出：百度

# 解法二：先将变量声明 使用关键字 global 声明成全局的，然后再修改

def test2():
    global name;
    name = "搜狐"
    print("func in name: ", name)

test2()                                         # 输出：搜狐
print("outer name: ", name)                     # 输出：搜狐





