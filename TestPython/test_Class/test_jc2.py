#coding=utf8

class test1(object):
    a1 = '123'
    def __init__(self, v):
        self.value1 = v

    def ppp(self):
        print self.value1

class test2(test1):
    pass
    def __init__(self, v):
        super(test2, self).__init__(v)
        self.value2 = v + '---'
        self.p1()

    def ppp(self, p):
        print self.value1 + "+++" + p
        print self.value2 + "+++" + p

    def p1(self):
        print 'p1'

# O1 = test1('www')
# O1.ppp()

O2 = test2('xxx')
O2.ppp('www')
