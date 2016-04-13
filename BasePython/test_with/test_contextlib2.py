#coding=utf8
from contextlib import contextmanager
from contextlib import nested
from contextlib import closing

@contextmanager
def make_context(name) :
    print 'enter', name
    yield name
    print 'exit', name

with nested(make_context('A'), make_context('B')) as (a, b):
    print a
    print b

print '\n---------------------\n'
with make_context('A') as a, make_context('B') as b:   #nested已经过时了，with已经可以通过多个上下文的直接嵌套了
    print a
    print b

print '\n---------------------\n'
class Door(object) :
    def open(self) :
        print 'Door is opened'
    def close(self) :
        print 'Door is closed'

with closing(Door()) as door :
    door.open()
