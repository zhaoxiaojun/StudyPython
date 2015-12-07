#coding=utf8
import threading

'''
Timer（定时器）是Thread的派生类，用于在指定时间后调用一个方法。
构造方法：
Timer(interval, function, args=[], kwargs={})
interval: 指定的时间
function: 要执行的方法
args/kwargs: 方法的参数
'''

def func():
    print 'hello timer!'

timer = threading.Timer(5, func)
timer.start()
print 11111111
