#coding=utf8
"""
装饰模式
定义：动态地为对象增加额外的职责
类型：结构型模式
"""

#展示一个人一件一件穿衣服的过程

class Person:
    def __init__(self,tname):
        self.name = tname
    def Show(self):
       print "dressed %s" %(self.name)

class Finery(Person):
    componet = None
    def __init__(self):
        pass
    def Decorate(self,ct):
        self.componet = ct
    def Show(self):
        if(self.componet!=None):
            self.componet.Show()

class TShirts(Finery):
    def __init__(self):
        pass
    def Show(self):
        print "Big T-shirt "
        self.componet.Show()

class BigTrouser(Finery):
    def __init__(self):
        pass
    def Show(self):
        print "Big Trouser "
        self.componet.Show()

if __name__ == "__main__":
    p = Person("somebody")
    bt = BigTrouser()
    ts = TShirts()
    bt.Decorate(p)
    ts.Decorate(bt)
    ts.Show()
