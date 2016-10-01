#coding=utf8

from threading import Thread, Lock
import time

lock = Lock()

class CreateListThread(Thread):
    def run(self):
        self.entries = []
        for i in range(10):
            time.sleep(0.01)
            self.entries.append(i)
        lock.acquire()     #加锁保证操作的原子性
        print self.entries
        lock.release()
        '''
        如果不加锁，当一个线程正在打印的时候，cpu切换到了另一个线程，所以产生了不正确的结果。我们需要确保print self.entries是个逻辑上的原子操作，以防打印时被其他线程打断
        '''

def use_create_list_thread():
    for i in range(3):
        t = CreateListThread()
        t.start()

use_create_list_thread()
