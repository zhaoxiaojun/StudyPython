#coding=utf8
import gevent

def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')

def thr(x):
    print('Explicit context to thr')
    gevent.sleep(x)
    print('Implicit context switch back to thr')


worklist = [gevent.spawn(foo), gevent.spawn(bar), gevent.spawn(thr, 0)]
gevent.joinall(worklist)
