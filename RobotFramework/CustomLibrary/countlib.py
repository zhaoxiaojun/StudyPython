#coding=utf-8
import sys
from robotremoteserver import RobotRemoteServer

#远程自定义关键字库 任意地方启动该库文件后即可使用（使用时需要指定ip和port）
#启动命令： python countlib.py  192.168.99.184 8271  默认127.0.0.1 8270


class countlib:
	def add(self,a,b):
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
	CL = countlib()
	RobotRemoteServer(CL, *sys.argv[1:])
