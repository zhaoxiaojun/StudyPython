#coding=utf8
"""
策略模式
定义：定义一组算法，将每个算法都封装起来，并且使他们之间可以互换
类型：行为类模式
"""
#商场收银软件，需要根据不同的销售策略方式进行收费

class CashSuper(object):
    def AcceptCash(self,money):
        return 0

class CashNormal(CashSuper):
    def AcceptCash(self,money):
        return money

class CashRebate(CashSuper):
    discount = 0
    def __init__(self,ds):
        self.discount = ds
    def AcceptCash(self,money):
        return money * self.discount

class CashReturn(CashSuper):
    total = 0;
    ret = 0;
    def __init__(self,t,r):
        self.total = t
        self.ret = r
    def AcceptCash(self,money):
        if (money>=self.total):
            return money - self.ret
        else:
            return money

class CashContext(object):
    def __init__(self,csuper):
        self.cs = csuper
    def GetResult(self,money):
        return self.cs.AcceptCash(money)

if __name__ == "__main__":
    money = input("money:")
    strategy = {}
    strategy[1] = CashContext(CashNormal())  #原价
    strategy[2] = CashContext(CashRebate(0.8))  #八折
    strategy[3] = CashContext(CashReturn(300,100))  #买满300减100
    ctype = input("type:[1]for normal,[2]for 80% discount [3]for 300 -100.")
    if ctype in strategy:
        cc = strategy[ctype]
    else:
        print "Undefine type.Use normal mode."
        cc = strategy[1]
    print "you will pay:%d" %(cc.GetResult(money))

