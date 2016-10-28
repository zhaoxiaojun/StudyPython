#coding=utf8
from testp import Runtest

__version__ = '0.1'
class CustomLibrary(Runtest):
	"""
		这里也可以装 x 的写上我们创建的 CustomLibrary 如何如何。
	"""
	ROBOT_LIBRARY_SCOPE = 'GLOBAL'   #作用域： TEST CASE     TEST SUITE   GLOBAL
