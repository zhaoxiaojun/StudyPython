#coding=utf8

class test1(object):
    def ppp(self):
        print self.name

class test2(object):
    age = 23

class test3(test2,test1):
    def __init__(self, name):
        self.name = name

    def ttt(self):
        print self.age



o = test3('nihao')
o.ppp()
o.ttt()
