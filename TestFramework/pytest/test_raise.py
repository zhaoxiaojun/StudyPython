#coding=utf8
import py.test

#断言异常

def testt():
    py.test.raises(ZeroDivisionError, "1 / 0")
