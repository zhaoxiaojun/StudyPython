#coding=utf8
import time

def timeit(func):
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print 'used:', end - start
    return wrapper

@timeit
def foo():
    print 'in foo()'

foo()

print '\n---内置装饰器---'
class Rabbit(object):

    def __init__(self, name):
        self._name = name

    @staticmethod    #静态方法
    def newRabbit(name):
        return Rabbit(name)

    @classmethod   #类方法
    def newRabbit2(cls):
        return Rabbit('')

    @property    #类属性
    def name(self):
        return self._name



print '\n---functools---'
import functools

def timeit(func):
    @functools.wraps(func)   #如果注释这一行，foo.__name__将是'wrapper'
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print 'used:', end - start
    return wrapper

@timeit
def foo():
    print 'in foo()'

foo()
print foo.__name__
