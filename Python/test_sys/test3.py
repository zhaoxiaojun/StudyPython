#coding=utf8
import sys


def exitfunc(value):
    print value
    sys.exit(0)  #0是正常退出

print "hello"

try:
    sys.exit(1000)    #sys.exit从python程序中退出，将会产生一个systemExit异常
except SystemExit,value:
    exitfunc(value)

print "come?"
