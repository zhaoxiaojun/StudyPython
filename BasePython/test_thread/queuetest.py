#coding=utf8
# 队列   线程同步
import threading
import time
import Queue

class producer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)
    def run(self):
        global queue
        queue.put(self.getName())
        print self.getName(),'put ',self.getName(), ' to queue'

class consumer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)
    def run(self):
        global queue
        print self.getName(),'get ',queue.get(), ' from queue'

queue = Queue.Queue()
plist = []
clist = []

for i in range(10):
    p = producer('producer' + str(i))
    plist.append(p)

for i in range(10):
    c = consumer('consumer' + str(i))
    clist.append(c)

for i in plist:
    i.start()
    i.join()
    print queue.qsize()

for i in clist:
    i.start()
    i.join()
    print queue.qsize()
