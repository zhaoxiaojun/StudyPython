#coding=utf8
'''
python经典(老实)类
'''
import inspect

class D:
    print 'D'

class E:
    print 'E'

class F:
    print 'F'

class C(D, F):
    print 'C'

class B(E, D):
    print 'B'

class A(B, C):
    print 'A'


if __name__ == '__main__':
    print inspect.getmro(A)
