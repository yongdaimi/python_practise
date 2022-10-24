# 演示如何重写父中的方法

class Fish:
    def fishtype(self):
        print("鱼不是哺乳动物")



class JingYu(Fish):
    def fishtype(self):
        print("鲸鱼是哺乳动物")


fish = Fish()
fish.fishtype()

# 覆盖父类的重名方法， 若子类中存在着与父类重名的方法时，则会覆盖
jingyu = JingYu()
jingyu.fishtype()

# 仍然要调用父类的方法
Fish.fishtype(jingyu)

'''
输出：

鱼不是哺乳动物
鲸鱼是哺乳动物

'''

