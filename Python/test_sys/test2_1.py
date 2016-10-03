#coding=utf8
import sys


#重定向
from StringIO import StringIO
buff = StringIO()   #stringIO对象

temp = sys.stdout  #保存标准I/O流

sys.stdout = buff  #将标准I/O流重定向到buff对象

print 42, 'hello', 0.001

sys.stdout = temp #恢复标准I/O流

print buff.getvalue()

print 'end'



'''
重定向错误信息
'''

fsock = open('error.log', 'w')   # 打开存储调试信息的日志文件

sys.stderr = fsock    #将新打开的日志文件的文件对象赋值给stderr以重定向标准错误

raise Exception, 'this error will be logged'   #引发一个异常
'''
没有在屏幕上打印出任何东西,所有正常的跟踪信息已经写进error.log
注意既没有显式关闭日志文件，也没有将stderr设回最初的值。因为一旦程序崩溃 (由于引发的异常)，Python将替我们清理并关闭文件
'''
