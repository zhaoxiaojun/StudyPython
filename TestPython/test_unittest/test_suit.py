#coding=utf8
import unittest
import os
import sys

class Cadd(object):

    def add(self, a, b):
        return a + b


class MyTest(unittest.TestCase):
    def setUp(self):
        #self.verificationErrors = []      #错误信息保存数组
        #self.accept_next_alert = True     #是否继续接受下一个警告
        self.testO = Cadd()

    def tearDown(self):
        #self.assertEqual([], self.verificationErrors)
        pass

    def testCadd(self):
        self.assertEqual(self.testO.add(1,2), 3)


if __name__ == '__main__':
    tsuite = unittest.TestSuite()
    tsuite.addTest(MyTest("testCadd"))
    unittest.TextTestRunner(verbosity=2).run(tsuite)
