#coding=utf-8
import unittest
testdir = r'E:\Code\yzhselenium\test_project\testgf'


testlist = unittest.defaultTestLoader.discover(testdir,'test*.py',None)

if __name__ == '__main__':
    unittest.TextTestRunner().run(testlist)

