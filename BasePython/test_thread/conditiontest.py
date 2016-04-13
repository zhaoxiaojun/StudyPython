#coding=utf8
# 条件变量   线程同步
import threading, os


class producer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)
    def run(self):
        global x, con
        con.acquire()
        if x == 1000000:
            con.wait()
        else:
            for i in range(10000000):
                x = x  + 1
            con.notify()
        print x, threading.currentThread().getName()
        con.release()

class consumer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)
    def run(self):
        global x, con
        con.acquire()
        if x == 0:
            con.wait()
        else:
            for i in range(10000000):
                x = x  - 1
            con.notify()
        print x, threading.currentThread().getName()
        con.release()

con = threading.Condition()
x = 0
p = producer('producer')
c = consumer('consumer')
p.start()
c.start()
p.join()
c.join()
print x, threading.currentThread().getName()
