#coding=utf8
"""
观察者模式
定义：定义对象间一种一对多的依赖关系，使得当每一个对象改变状态，则所有依赖于它的对象都会得到通知并自动更新
类型：行为类模式
"""

class Observer:
    def __init__(self,strname,strsub):
        self.name = strname
        self.sub = strsub
    def Update(self):
        pass

class StockObserver(Observer):
    #no need to rewrite __init__()
    def Update(self):
        print "%s:%s,stop watching Stock and go on work!" %(self.name,self.sub.action)

class NBAObserver(Observer):
    def Update(self):
        print "%s:%s,stop watching NBA and go on work!" %(self.name,self.sub.action)

class SecretaryBase:
    def __init__(self):
        self.observers = []
    def Attach(self,new_observer):
        pass
    def Notify(self):
        pass

class Secretary(SecretaryBase):
    def Attach(self,new_observer):
        self.observers.append(new_observer)
    def Notify(self):
        for p in self.observers:
            p.Update()

if __name__ == "__main__":
    p = Secretary()
    s1 = StockObserver("xh",p)
    s2 = NBAObserver("wyt",p)
    p.Attach(s1);
    p.Attach(s2);
    p.action = "WARNING:BOSS ";
    p.Notify()
