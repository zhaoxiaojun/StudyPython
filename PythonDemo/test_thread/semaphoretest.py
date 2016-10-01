#coding=utf8
#线程同步对象: 信号量 semaphore   线程同步
import threading, time, random

#数据生成
def  numbergen(sem, queue, qlock):
    while 1:
        time.sleep(2)
        if random.randint(0,1):
            value = random.randint(0, 100)
            qlock.acquire()
            try:
                queue.append(value)
            finally:
                qlock.release()
            print "%s: place %d on the queue" % (threading.currentThread().getName(), value)
            sem.release()

#数据处理
def numbercalc(sem, queue, qlock):
    while 1:
        sem.acquire()
        qlock.acquire()
        try:
            value = queue.pop(0)
        finally:
            qlock.release()
        print "%s: Got %d from the queue. " % (threading.currentThread().getName(), value)
        newvalue = value * 2
        time.sleep(3)

childthreads = []
sem = threading.Semaphore(0)
queue = []
qlock = threading.Lock()

t = threading.Thread(target=numbergen, args = [sem, queue, qlock])
t.setDaemon(1)
t.start()
childthreads.append(t)

for i in range(1,3):
    t = threading.Thread(target=numbercalc, args = [sem, queue, qlock])
    t.setDaemon(1)
    t.start()
    childthreads.append(t)

#while 1:
time.sleep(30)






