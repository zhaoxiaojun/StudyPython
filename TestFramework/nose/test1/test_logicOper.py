# -*- coding: utf-8 -*-
from nose.tools import assert_equal
from  func.logicOperator import  isGreaterThan

def test_logicOper_isGreaterThan():
    print("=================test_logicOper_isGreaterThan============")
    result = isGreaterThan(4,3)
    assert_equal(True, result)




'''
当前目录下执行：
nosetests -s
'''
