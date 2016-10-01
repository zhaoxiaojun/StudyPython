#coding=utf8
import inspect
import sys
from mmm import *


print sys.modules[__name__]

#获取test234模块中的所有类
name = 'test234'
print eval(name)
clsmembers = inspect.getmembers(eval(name), inspect.isclass)

for clsmember in clsmembers:
    print clsmember[0]
