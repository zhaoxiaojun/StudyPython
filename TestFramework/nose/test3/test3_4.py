#coding=utf8
from nose.tools import assert_equal
from nose.tools import with_setup

'''
测试方法的setup、teardown
'''

def start1():
    print('aaa')

def end1():
    print('bbb')

def start2():
    print(111)

def end2():
    print(222)

@with_setup(start1, end1)
@with_setup(start2, end2)
def test_masd_add():
    print('----')
    assert_equal(10, 10)
