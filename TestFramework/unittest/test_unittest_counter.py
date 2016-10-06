#coding=utf-8
from counter import counter
import unittest

class test_counter(unittest.TestCase):  #TestCase：所有测试用例的基本类
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

class test_counter2(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.subd = counter()

    def test_subtraction(self):
        self.vsub = self.subd.subtraction(10, 10)
        self.assertEqual(self.vsub, 0, 'test fail!')

    def test_subtraction2(self):
        self.vsub = self.subd.subtraction(8.9, 5.4)
        self.assertEqual(self.vsub, 3.5, 'test fail!')

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        pass

if __name__ == '__main__':
    #unittest.main() #通过框架的main方法执行测试用例
    '''
    main： 其实就是TestProgram
    TestProgram：命令行进行单元测试的调用方法，作用是执行一个测试用例。其实unittest.main()方法执行的就是这个命令，而这个类实例时默认加载当前
    执行的作为测试对象，原型为 __init__(self, module='__main__', defaultTest=None, argv=None, testRunner=xx, testLoader=xx)  其中
    module='__main__'就是默认加载自身
    '''

    #构造测试集：定义测试套
    tsuite = unittest.TestSuite()  #TestSuite：组织测试用例的实例，支持测试用例的添加和删除，最终将传递给testRunner进行执行

    #构造测试集：向测试套中装载测试用例
    tsuite.addTest(test_counter("test_add"))
    tsuite.addTest(test_counter("test_add1"))
    tsuite.addTest(test_counter("test_add2"))

    tsuite.addTest(test_counter2("test_subtraction"))
    tsuite.addTest(test_counter2("test_subtraction2"))

    #执行测试
    trunner = unittest.TextTestRunner   #TextTestRunner：进行测试用例执行的实例，其中Text的意思是以文本形式显示测试结果
    trunner.run(tsuite)

