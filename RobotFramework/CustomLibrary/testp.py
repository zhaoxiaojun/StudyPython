#coding=utf8
'''
created by defias
'''
#使用方法：
#本地自定义关键字库，将库目录（CustomLibrarty模块 包含__init__.py文件）置于python的模块目录/Library/Python/2.7/site-packages下，然后ride中导入即可使用

__version__ = '0.1'
from robot.api import logger

class Runtest(object):   #Runtest这个名字不能修改(固定的)
	def runtest(self):   #Runtest中的方法就是robotframework中可以使用的关键字
		u'''
		this is a test
		'''
		print 'this is a testing'
		logger.debug("debug: xxxx")

    def runtest2(self):
        import time
        print time.time()

# if __name__ == '__main__':
# 	Runtest().runtest()
