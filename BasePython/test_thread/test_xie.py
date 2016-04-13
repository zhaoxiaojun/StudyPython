#coding=utf8
#线程同步对象: 信号量 semaphore   线程同步
import threading, time, random


#数据写入
def  numbergen(qlock):
    global queue
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

queue = []
qlock = threading.Lock()

for i in range(1,3):
    t = threading.Thread(target=numbergen, args = [qlock])
    t.setDaemon(1)
    t.start()

#while 1:
time.sleep(30)






