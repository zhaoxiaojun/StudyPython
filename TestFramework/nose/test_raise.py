#coding=utf8
import nose.tools


#断言异常

def div(x, y):
    return x/y


def test_div():
    nose.tools.assert_raises(ZeroDivisionError, div, 1, 0)
