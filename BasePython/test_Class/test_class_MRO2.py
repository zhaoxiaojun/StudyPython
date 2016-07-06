#coding=utf8
#C3算法
import inspect

class D(object):
    print 'D'

class E(object):
    print 'E'

class F(object):
    print 'F'

class C(D, F):
    print 'C'

class B(E, D):
    print 'B'

class A(B, C):
    print 'A'


if __name__ == '__main__':
    #print A.__mro__
    print inspect.getmro(A)
