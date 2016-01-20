#coding=utf8
from ggg import *
import threading
import time
import mmm

class subc(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print 'sleep 3s...\n'
        time.sleep(3)
        print 'sleep 3s end\n'

        print '%s set event...' % threading.currentThread().getName()
        event.set()
        print '%s set event end' % threading.currentThread().getName()


t2 = mmm.mmm()
t2.setDaemon(True)
t2.start()


t1 = subc()
t1.setDaemon(True)
t1.start()


t2.join()
print '---'
