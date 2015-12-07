#coding=utf-8
import threading        #引入线程模块
from time import sleep, ctime
import time

#音乐播放器
def music(func):
    for i in range(3):
        print "I was listening to %s! %s" %(func,ctime())
        sleep(2)

#视频播放器
def move(func):
    for i in range(3):
        print "I was at the %s! %s" %(func,ctime())
        sleep(3)

#创建线程队列用于装载线程
threads = []

#创建线程
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
t2 = threading.Thread(target=move,args=(u'阿凡达',))

#添加到线程数组
threads.append(t1)
threads.append(t2)


if __name__ == '__main__':
    for i in threads:
        i.start()     #启动线程

    '''
    threads[0].start()
    print 1111
    time.sleep(3)
    print 2222
    threads[1].start()
    '''

    for i in threads:
        i.join()      #守护线程，等待线程终止

    '''
    threads[0].join()
    threads[1].join()
    '''
    print 'all end: %s' %ctime()
