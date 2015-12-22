#coding=utf-8
import unittest

def create_testsuite():
    #定义测试套
    tsuite = unittest.TestSuite()
    
    #定义测试文件查找目录
    test_dir = r'E:\Code\yzhUT\study_unittest\testcase'
    
    #定义 discover 方法的参数
    testlist = unittest.defaultTestLoader.discover(test_dir,pattern ='test*.py',top_level_dir=None)

    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in testlist:
        for test_case in test_suite:
            tsuite.addTests(test_case)
            #print tsuite
    return tsuite

if __name__ == '__main__':
    runner =unittest.TextTestRunner()
    runner.run(create_testsuite())