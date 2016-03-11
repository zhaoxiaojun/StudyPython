#coding=utf8

class test1(object):
    a1 = '123'
    def __init__(self, v):
        self.value1 = v

    def ppp(self):
        print self.value1

class test2(test1):
    # def __init__(self, v):
    #     self.value1 = v + '---'

    def ppp(self, p):
        print self.value1 + "+++" + p

O1 = test1('www')
O1.ppp()

O2 = test2('qqq')
O2.ppp()
