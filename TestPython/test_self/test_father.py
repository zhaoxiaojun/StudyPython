#coding=utf8
import inspect

'''
inspect.stack():
第一列是对象名，第二列是当前脚本文件名，第三列是行数，第四列是函数名，第五列是具体执行的程序。
第一行是当前函数，第二行是父级函数，。。以此往上钻取，基本上只有前两三行有用。
'''

def f1():
    f2()

def f2():
    print 'caller name:', type(inspect.stack()[1][1])
    print 'caller name:', type(inspect.stack()[1][2])

f1()
