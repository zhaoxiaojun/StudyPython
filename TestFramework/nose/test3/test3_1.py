#coding=utf8

def setup_module(module):
    print('setup_module函数')


def teardown_module(module):
    print('teardown_module函数')



def testmm():
    assert 1 == 1


def testvv():
    assert 2 == 2


'''
module的setup 、teardown的设置
在整个测试的运行期间只运行一次
setup函数的取名可以是： setup, setup_module, setUp or setUpModule中的一个
teardown函数取名可以是： teardown, teardown_module or tearDownModule中的一个
'''
