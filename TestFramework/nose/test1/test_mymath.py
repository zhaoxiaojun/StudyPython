# -*- coding: utf-8 -*-
from nose.tools import assert_equal
from nose.tools import with_setup
import  unittest
from func.mymath import mmath

def setUp():
    print("============test math module setup==============")

def teardown():
    print("============test math module teardown==============")

def test_math_add():
    result = mmath.add(4, 5)
    print("================test_math_add============")
    assert_equal(9, result)


class test_math3():
    def setUp(self):
        print("============test math class setup==============")

    def teardown(self):
        print("============test math class teardown==============")

    def test_math_square(self):
        print("=============== test_math_square================ ")
        assert_equal(9, mmath.square(3))

    def test_math_sub(self):
        print("=============== test_math_sub================ ")
        assert_equal(1, mmath.sub(3, 2))


class test_math2(unittest.TestCase):
    def test_math_multipy(self):
        print("=============== test_math_multipy================ ")
        assert_equal(8, mmath.multiply(2, 4))




