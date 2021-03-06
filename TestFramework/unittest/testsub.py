#coding=utf-8
from counter import counter
import unittest

class test_counter2(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.subd = counter()

    def test_subtraction(self):
        self.vsub = self.subd.subtraction(10, 10)
        self.assertEqual(self.vsub, 10, 'test fail!')

    def test_subtraction2(self):
        self.vsub = self.subd.subtraction(8.9, 5.4)
        self.assertEqual(self.vsub, 3.5, 'test fail!')

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        pass

if __name__ == '__main__':
    #unittest.main() #通过框架的main方法执行测试用例，默认执行以test开头的方法

    #构造测试套
    tsuite = unittest.TestSuite()

    #向测试套中装载测试用例
    tsuite.addTest(test_counter2("test_subtraction"))
    tsuite.addTest(test_counter2("test_subtraction2"))

    #执行测试
    trunner = unittest.TextTestRunner
    trunner.run(tsuite)

