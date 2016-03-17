#coding=utf8
import gevent
import random
import time

def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(random.randint(0,3)*0.5)
    print('Task %s done' % pid)

def synchronous():
    for i in range(1,10):   #同步执行
        task(i)

def asynchronous():
    threads = [gevent.spawn(task, i) for i in xrange(10)]   #异步执行
    gevent.joinall(threads)




if __name__ == '__main__':
    print  '测试开始时间: ',time.strftime("%Y-%m-%d %H:%M:%S")
    now = time.time()

    print('Synchronous:')
    synchronous()

    print  '测试结束时间: ',time.strftime("%Y-%m-%d %H:%M:%S")
    end = time.time()
    print  '时长: ',  end-now


    print  '测试开始时间: ',time.strftime("%Y-%m-%d %H:%M:%S")
    now = time.time()

    print('Asynchronous:')
    asynchronous()

    print  '测试结束时间: ',time.strftime("%Y-%m-%d %H:%M:%S")
    end = time.time()
    print  '时长: ',  end-now
