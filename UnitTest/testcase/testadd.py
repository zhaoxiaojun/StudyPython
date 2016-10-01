#coding=utf-8
from counter import counter
import unittest

class test_counter(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.add = counter()

    def test_add(self):
        self.vadd = self.add.add(1,99)
        self.assertEqual(self.vadd, 100, 'test fail!')

    def test_add1(self):
        self.vadd = self.add.add(0.1,0.9)
        self.assertEqual(self.vadd, 1.0, 'test fail!')

    def test_add2(self):
        self.vadd = self.add.add('hello',' world!')
        self.assertEqual(self.vadd, 'hello world!', 'test fail!')

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        pass

# 构造测试集
def addsuite1():
    suite = unittest.TestSuite()
    suite.addTest(test_counter("test_add"))
    suite.addTest(test_counter("test_add1"))
    return suite

def addsuite2():
    suite = unittest.TestSuite()
    #suite.addTest(test_counter("test_add2"))
    return suite

def alltests():
    suite = unittest.TestSuite((addsuite1(), addsuite2()))
    return suite

if __name__ == '__main__':
    #unittest.main() #通过框架的main方法执行测试用例，默认执行以test开头的方法

    #unittest.main(defaultTest = 'addsuite1')
    unittest.TextTestRunner().run(alltests())

