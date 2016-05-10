#coding=utf8
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, tdname):
        threading.Thread.__init__(self, name=tdname)

    def run(self):
        time.sleep(5)
        print '[%s]' % self.getName()
        #global idd
        #idd = True
        #print "idd is: %s" % str(idd)

if __name__ == "__main__":
    #idd = False
    tdname = 'ttt'
    t1=MyThread(tdname)
    #t1.setDaemon(True)   #setDaemon的默认值是False

    t2=MyThread(tdname)
    t2.setDaemon(True)

    t1.start()
    t2.start()

    print "I am the father thread."
    #while not idd:
        #time.sleep(1)
        #print '...'

    print threading.activeCount() #返回正在运行的线程数量 与len(threading.enumerate())有相同的结果
    print threading.enumerate()  #返回一个包含正在运行的线程的list

    print 'father end'
