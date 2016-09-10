#coding=utf8
import inspect


class c1(object):
    def f1(self):
        print inspect.stack()


o1 = c1()
o1.f1()

print ''
print ''

class c2(object):
    #print inspect.stack()
    classname = inspect.stack()[0][3]
    print classname
    filename = inspect.stack()[0][1][:-3]
    print filename

c2()
