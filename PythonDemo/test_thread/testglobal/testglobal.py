#coding=utf8
from ggg import *
import ggg
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

        #global ggg.isflag
        print 'subc isflag id: ', id(ggg.isflag)
        ggg.isflag = True
        print 'subc isflag: ', ggg.isflag


t2 = mmm.mmm()
t2.setDaemon(True)
t2.start()


t1 = subc()
t1.setDaemon(True)
t1.start()


t2.join()
print '---'
