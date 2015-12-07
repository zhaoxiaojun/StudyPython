#coding=utf8
import threading
import time

class mythread(threading.Thread):
    def __init__(self,threadname,singal):
        threading.Thread.__init__(self,name=threadname)
        self.singal = singal

    def run(self):
        while True:
            print 'singal: ',self.singal.isSet()
            time.sleep(1)

        '''
        if self.singal.isSet():
            self.singal.clear()
            self.singal.wait()
            print self.getName()
        else:
            print self.getName()
            self.singal.set()
        '''
singal = threading.Event()

singal.set()

t1=[]

for i in range(1):
    t=mythread(str(i),singal)
    t1.append(t)

for i in t1:
    i.start()

time.sleep(3)
singal.clear()
time.sleep(3)
singal.set()
