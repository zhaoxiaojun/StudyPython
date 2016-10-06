#coding=utf-8
import unittest

def create_testsuite():
    #定义测试套
    tsuite = unittest.TestSuite()

    #定义测试文件查找目录
    test_dir = r'E:\Code\yzhUT\study_unittest\testcase'

    #定义discover方法的参数
    testlist = unittest.defaultTestLoader.discover(test_dir,pattern ='test*.py',top_level_dir=None)
    '''
    defaultTestLoader：其实就是TestLoader
    TestLoader：测试用例加载器，其包括多个加载测试用例的方法, 返回一个测试套件
    loadTestsFromModule(self, module)  --根据给定的模块实例来获取测试用例套件
    loadTestsFromName(self, name, module=None)  --根据给定的字符串来获取测试用例套件，字符串可以是模块名，测试类名，测试类中的测试方法名，或者一个可调用的是实例对象,这个实例对象返回一个测试用例或一个测试套件
    loadTestsFromNames(self, names, module=None)  --和上面功能相同，只不过接受的是字符串列表
    loadTestsFromTestCase(self, testCaseClass)   --根据给定的测试类，获取其中的所有测试方法，并返回一个测试套件
    discover
    '''

    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in testlist:
        for test_case in test_suite:
            tsuite.addTests(test_case)
            #print tsuite
    return tsuite

if __name__ == '__main__':
    runner =unittest.TextTestRunner()
    runner.run(create_testsuite())


