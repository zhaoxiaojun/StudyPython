#coding=utf8
import multiprocessing
import time
from io import StringIO

class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):   #还在主进程
        multiprocessing.Process.__init__(self)
        self.interval = interval
        print '__init__'

    def run(self):           #进入子进程
        print 'run'
        n = 5
        #MEMdata = StringIO()
        #MEMdata.write(u'sdfsdfsdfsdfsdfsdfsdfsdf')
        while n > 0:
            print("the time is {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1

if __name__ == '__main__':
    p = ClockProcess(3)
    print 1111111111111
    p.start()
