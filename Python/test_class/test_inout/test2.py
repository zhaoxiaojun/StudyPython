#coding=utf8


#内部类

class outter(object):
    def __init__(self,name):
        self.name = name

    def a(self):
        innerO = self.inner(self)
        innerO.test()

    class inner:
        out = None
        def __init__(self, out=None):
            self.out = out

        def test(self):
            print self.out.name


t = outter('hello world!')
t.a()
