#coding=utf8
# 线程锁  线程同步
import threading, time

b = 50
I =  threading.Lock()  #线程锁对象

def threadcode():
    I.acquire()  #取得一把锁  调用acquire([timeout])时，线程将一直阻塞，直到获得锁定或者直到timeout秒后（timeout参数可选）。返回是否获得锁。
    global b
    print "thread %s invoked" % threading.currentThread().getName()
    try:
        print "thread %s running" % threading.currentThread().getName()
        time.sleep(3)
        b = b+50
        print "thread %s set b to %d" % (threading.currentThread().getName(), b)
    finally:
        I.release()  #释放锁

print "Value of b at start of program:", b

childthread = []

for i in range(1,5):
    t = threading.Thread(target=threadcode, name='thread-%d' % i)
    t.setDaemon(1)
    t.start()
    print 'thread %d' % 111111
    childthread.append(t)

for t in childthread:
    t.join()

print 'new value of b:', b
