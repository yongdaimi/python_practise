# 演示枚举类的用法

# python 中创建枚举类有两种方式：
# 1. 使当前类继承于 Enum 类；
# 2. 使用Enum 函数动态创建

# 使用Python中的枚举类，需要引入 enum 模块
# from enum import Enum

# 如果需要保证枚举类中的值唯一，需要导入unique 装饰器
# from enum improt Enum, unique


# 例一： 继承Enum类：

from enum import Enum, unique


class Sex(Enum):
    Man = 0
    Woman = 1

print("Man info, Man.name: %s, Man.value: %d" %(Sex.Man.name, Sex.Man.value))
print("Woman info, Woman.name: %s, Woman.value: %d" %(Sex.Woman.name, Sex.Woman.value))


# 例二：使用Enum() 函数, 第一个参数代表类名，第二个参数是一个元组，代表枚举值

Sex = Enum("Sex", ('Man', 'Woman'))

print("Sex.Man的值是：", Sex['Man'].value)
print("Sex.Woman的值是：", Sex['Woman'].value)

'''
貌似使用这种方式，Enum的值是从 1 开始的。。。
'''

# 例三: 不允许Enum中的值发生重复

# 默认情况下，Enum中定义的值是允许重复的，比如：

class Color(Enum):
    RED = 1
    GREEN = 1
    BLUE = 3

print("RED Color value: ", Color.RED.value)             # RED Color value:  1
print("GREEN Color value: ", Color.GREEN.value)         # GREEN Color value:  1


# 添加@unique装饰器可确保枚举类定义的值唯一

@unique
class Color(Enum):
    RED = 1
    GREEN = 2                                           # 若再将GREEN的值设为1，会报 ValueError: duplicate values found
    BLUE = 3

print("RED Color value: ", Color.RED.value)             # RED Color value:  1
print("GREEN Color value: ", Color.GREEN.value)         # GREEN Color value:  2
print("-----------------------------------------------------")


# 例四：枚举类提供了一个 __members__ 属性，该属性是一个包含了枚举类所有成员的字典，通过遍历该属性，可以访问枚举类中的所有成员

for name, member in Color.__members__.items():
    print(name, "->", member)

'''
RED -> Color.RED
GREEN -> Color.GREEN
BLUE -> Color.BLUE
'''


# 例五：枚举类不能比较大小，但是可以比较是否相等
print(Color.RED == Color.GREEN)                        # 输出：False
print(Color.RED.name is Color.GREEN.name)              # 输出：False

if (Color.RED > Color.GREEN):                          # 不允许对枚举值比较大小，会报：'>' not supported between instances of 'Color' and 'Color'
    print("RED > GREEN")