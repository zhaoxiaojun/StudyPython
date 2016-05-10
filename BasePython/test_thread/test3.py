#coding=utf8

import threading

class test3(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        inputi = raw_input('请输入：')

def fun1():
    t = test3()
    t.setDaemon(True)
    t.start()

fun1()
