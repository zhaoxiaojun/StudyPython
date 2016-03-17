#coding=utf8
from contextlib import contextmanager

@contextmanager   #通过Generator实现
def make_context() :
    print 'enter'
    try :
        yield {}
    except RuntimeError, err :
        print 'error' , err
    #finally :
    print 'exit'

with make_context() as value :
    print value

