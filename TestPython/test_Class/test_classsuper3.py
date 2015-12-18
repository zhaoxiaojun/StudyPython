#coding=utf8


class A(object):
    def __init__(self):
        print "enter A"
        print "leave A"

class B(A):
    def __init__(self):
        print "enter B"
        super(B, self).__init__()
        print "leave B"

class C(A):
    def __init__(self):
        print "enter C"
        super(C, self).__init__()
        print "leave C"

class D(B, C):
    pass

'''
class D(B, C):
    def __init__(self):
        pass
'''


print D.__mro__

d = D()
