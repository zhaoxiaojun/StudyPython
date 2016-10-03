#coding=utf-8
import unittest

#定义测试文件查找目录
test_dir = r'E:\Code\yzhUT\study_unittest\testcase'
    
testlist = unittest.defaultTestLoader.discover(test_dir,pattern ='test*.py',top_level_dir=None)

if __name__ == '__main__':
    runner =unittest.TextTestRunner()
    runner.run(testlist)