#coding=utf-8
import unittest
#加载测试文件
import testadd
import testsub
# 构造测试集
suite = unittest.TestSuite()

suite.addTest(testadd.test_counter("test_add"))
suite.addTest(testadd.test_counter("test_add1"))
suite.addTest(testadd.test_counter("test_add2"))

suite.addTest(testsub.test_counter2("test_subtraction"))
suite.addTest(testsub.test_counter2("test_subtraction2"))

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)