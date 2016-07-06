#coding=utf8
'''
单例模式
定义：确保一个类只有一个实例，而且自行实例化并向整个系统提供这个实例
类型：创建类模式
'''

"""
方法1： 实现__new__方法
将一个类的实例绑定到类变量_inst上,如果cls._inst为None说明该类还没有实例化过,实例化该类,并返回，如果cls._inst不为None,直接返回cls._inst
"""

class Singleton(object):
    print 'test11111111111'
    def __new__(abc, *a, **k):
        if not hasattr(abc, '_ascinst'):
            abc._ascinst = super(Singleton, abc).__new__(abc, *a, **k)
            #abc._ascinst = object.__new__(abc, *a, **k)
        return abc._ascinst

    def ppp(self,s):
        return s



a = Singleton()
a.toto = 12
b = Singleton()

print b.toto

print id(a), id(b)  # The same !!

print a.ppp('aaa')
print b.ppp('bbb')

print a == b

print a is b



