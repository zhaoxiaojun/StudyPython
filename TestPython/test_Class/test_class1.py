#coding=utf8

class Employee:
    pass

lee = Employee()
lee.name = 'leefang'
lee.age = 28


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class cAA:
    i = 8

    def __init__(self):
        self.__a = 7
        self.m_a = 1
        self.m_b = 2

    def __Method1(self):
        self.__a += 1
        return self.__a

    def Method2(self, _x):
        print self.__Method1(), _x

class cCC:
    def Method2(self,_x):
        print 'aaaaaaaaa'

class cBB(cCC, cAA):
    def kk(self, _x):
        self.Method2(_x)

    def tt(self):
        print self.m_a


b = cBB()
b.Method2(4)
b.kk('ffffff')
b.tt()

