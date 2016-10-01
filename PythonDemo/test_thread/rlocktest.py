#coding=utf8
# 可重入锁
'''
RLock是可重入锁（reentrant lock），acquire()能够不被阻塞的被同一个线程调用多次。要注意的是release()需要调用与acquire()相同的次数才能释放锁。
'''

import threading
import time

rlock = threading.RLock()

def func():
    # 第一次请求锁定
    print '%s acquire lock...' % threading.currentThread().getName()
    if rlock.acquire():
        print '%s get the lock.' % threading.currentThread().getName()
        time.sleep(2)

        # 第二次请求锁定
        print '%s acquire lock again...' % threading.currentThread().getName()
        if rlock.acquire():
            print '%s get the lock.' % threading.currentThread().getName()
            time.sleep(2)

        # 第一次释放锁
        print '%s release lock...' % threading.currentThread().getName()
        rlock.release()
        time.sleep(2)

        # 第二次释放锁
        print '%s release lock...' % threading.currentThread().getName()
        rlock.release()

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)
t1.start()
t2.start()
t3.start()
