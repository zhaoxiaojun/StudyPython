#coding=utf8
import threading
import time


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(5)
        global idd
        idd = True
        print "idd is: %s" % str(idd)

if __name__ == "__main__":
    idd = False
    t1=MyThread()
    t1.setDaemon(True)   #setDaemon的默认值是False
    t1.start()
    print "I am the father thread."
    while not idd:
        time.sleep(1)
        print '...'
    print 'father end'
