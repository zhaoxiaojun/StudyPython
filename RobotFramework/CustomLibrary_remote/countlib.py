#coding=utf-8
import sys
from robotremoteserver import RobotRemoteServer

'''
robotremoteserver是一种远程库接口技术（remote library interface）, robotremoteserver可以启动一个Library给Robot Framework用，不管这个库在本机的任何位置，
或远程的某台主机上，或者这个库不是Python开发的

启动命令： python countlib.py  192.168.99.184 8271  默认127.0.0.1 8270
RobotFramework提供的libdoc工具用于生成一份测试库文档: python -m robot.libdoc -f html countlib.py  countlib.html
'''

class countlib_yzh(object):
	def add(self,a,b):    #方法即是robotframwork中可以使用的关键字
		'''Computing a and b are two numbers together, for example:
		|    add     |   2    |    5     |
		'''
		return a + b

	def sub(self,a,b):
		'''Computing a and b subtract two numbers, for example:
		|    sub     |   10    |    2     |
		'''
		return a - b


if __name__ == '__main__':
	CL = countlib_yzh()
	RobotRemoteServer(CL, *sys.argv[1:])
