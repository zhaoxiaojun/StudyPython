#coding=utf8
from ggg import *
import threading
import time


class mmm(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print '%s wait for event...' % threading.currentThread().getName()
        event.wait()
        print '%s recv event.' % threading.currentThread().getName()

        print 'dodododododododododo'
