#coding=utf-8
from counter import counter
import unittest
from unittest import *
from m_unit import *

class Test(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        def isParameterizedMethod(attrname):
            return attrname.startswith("parameterized") and hasattr(getattr(self, attrname), '__call__')

        testFnNames = filter(isParameterizedMethod, dir(self))
        for func in testFnNames:
            name = func.split("_", 1)[1]
            collect = "collection_" + name
            if hasattr(getattr(self, collect), '__call__'):
                collectFunc = getattr(self, collect)
                array = collectFunc()
                for index in xrange(len(array)):
                    test = "%s_%d" % (name, index)
                    setattr(self.__class__, test, getattr(self, func)(array[index]))
        # must called at last  
        unittest.TestCase.__init__(self, methodName)

class Loader(unittest.TestLoader):
    def getTestCaseNames(self, testCaseClass):
        """    Return a sorted sequence of method names found within testCaseClass """
        testFnNames = unittest.TestLoader.getTestCaseNames(self, testCaseClass)

        def isParameterizedMethod(attrname, testCaseClass=testCaseClass, prefix="parameterized"):
            return attrname.startswith(prefix) and hasattr(getattr(testCaseClass, attrname), '__call__')

        testFnNames0 = filter(isParameterizedMethod, dir(testCaseClass))
        for func in testFnNames0:
            name = func.split("_", 1)[1]
            collect = "collection_" + name
            if hasattr(getattr(testCaseClass, collect), '__call__'):
                collectFunc = getattr(testCaseClass, collect)
                for item in xrange(len(collectFunc())):
                    testFnNames.append("%s_%d" % (name, item))

        if self.sortTestMethodsUsing:
            testFnNames.sort(key=_CmpToKey(self.sortTestMethodsUsing))

        return testFnNames

class test_counter(Test):
    @classmethod
    def collection_test_add(cls):
        return [1,2,3,4]

    def parameterized_test_add(self,x):
        def test_body(self):
            print(x * y)
        return test_body





if __name__ == '__main__':
    #unittest.main() #通过框架的main方法执行测试用例，默认执行以test开头的方法

    #构造测试集：定义测试套
    #tsuite = unittest.TestSuite()

    #构造测试集：向测试套中装载测试用例
    #tsuite.addTest(test_counter("test_add"))
    #tsuite.addTest(test_counter("test_add1"))
    #tsuite.addTest(test_counter("test_add2"))
    #tsuite.addTest(test_counter2("test_subtraction"))
    #tsuite.addTest(test_counter("test_add2"))
    #tsuite.addTest(test_counter2("test_subtraction2"))

    #执行测试
    #ttr=unittest.TextTestRunner(verbosity=2)
    #ttr.run(tsuite)

    #构造测试集：向测试套中装载测试用例类
    suite1 = Loader().loadTestsFromTestCase(test_counter)  
    #suite2 = unittest.TestLoader().loadTestsFromTestCase(test_counter2)  
    #suite = unittest.TestSuite([suite1])
    rc = unittest.TextTestRunner(verbosity=2).run(suite1)
    print rc

