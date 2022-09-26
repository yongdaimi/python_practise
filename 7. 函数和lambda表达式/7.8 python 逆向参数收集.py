# 正向参数收集指的是函数可以接收任意多的参数，非关键字参数会存储到元组中，关键字参数会存储到字典中；
# 逆向参数收集指的是函数可以直接接收序列(列表、元组、字典)，当收到这些参数时，python会将其进行拆分，将其中存储的参数按照次序分给函数中的各个形参

# 在使用逆向参数收集时，python语法规定，当传入的是列表或元组时，其名称前需要加一个*号，前传入字典时，其前面需要加两个*号

# 例一： 向函数中传入一个列表
def detail_info(name, address):
    print("name type: ", type(name), ", address type: ", type(address))
    print("name: ", name, ", address: ", address)
    print("%s的地址是%s" %(name, address))

person = ["Zhangsan", "China-JiangSu"]
detail_info(*person)


# 例二：向函数中传入一个字典 (注意：字典前需要加入两个分号)
def detail(name, address):
    print("name: ", name)
    print("address: ", address)

data = {"name":"百度", "address":"http://www.baidu.com"}
detail(**data)

# 例三：给可变参数传参
print("------------------------- 给可变参数传参 -------------------------------")
def teams_info(teams_name, *teams_members):
    print("Teams Name: ", teams_name)
    print("Members:")
    for m in teams_members:
        print(m)


OG = ["OG", "ana", "Topson", "Ceb", "Jreax", "Notail"]
teams_info(*OG)

'''
输出：

Teams Name:  OG
Members:
ana
Topson
Ceb
Jreax
Notail

'''



