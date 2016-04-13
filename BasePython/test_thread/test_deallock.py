#coding=utf8
import threading, time

a = 5
b = 5
alock = threading.Lock()
block = threading.Lock()

def thread1code():
    print "thread1 acquire lock a"
    alock.acquire()
    time.sleep(5)

    print "thread1 acquire lock b"
    block.acquire()
    time.sleep(5)
    global a, b
    a += 5
    b += 5

    print "thread1 release both locks"
    block.release()
    alock.release()

def thread2code():
    print "thread2 acquire lock a"
    alock.acquire()
    time.sleep(5)

    print "thread2 acquire lock b"
    block.acquire()
    time.sleep(5)
    global a, b
    a += 5
    b += 5

    print "thread2 release both locks"
    block.release()
    alock.release()


t = threading.Thread(target=thread1code)
t.setDaemon(True)
t.start()

t = threading.Thread(target=thread2code)
t.setDaemon(True)
t.start()

while True:
    time.sleep(30)

'''
避免死锁原则：
1. 以一个固定顺序取得锁
2. 按照与取得锁相反的顺序释放锁
'''
