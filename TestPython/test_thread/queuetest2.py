#coding=utf8
import random,threading,time
from Queue import Queue

#Producer thread
class Producer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self,name=t_name)
        self.data=queue
    def run(self):
        for i in range(10):    #随机产生10个数字 ，可以修改为任意大小
            randomnum=random.randint(1,99)
            print "%s: %s is producing %d to the queue!" % (time.ctime(), self.getName(), randomnum)
            #将一个值放入队列中。调用队列对象的put()方法在队尾插入一个项目。put()有两个参数，第一个item为必需的，为插入队列中的值；第二个block为可选参数，默认为1。如果队列当前已满且block为1，put()方法就使调用线程暂停,直到空出一个数据单元。如果block为0，put方法将引发Full异常
            self.data.put(randomnum)
            time.sleep(1)
        print "%s: %s finished!" %(time.ctime(), self.getName())

#Consumer thread
class Consumer_even(threading.Thread):
    def __init__(self,t_name,queue):
        threading.Thread.__init__(self,name=t_name)
        self.data=queue
    def run(self):
        while 1:
            try:
                #将一个值从队列中取出。调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。如果队列为空且block为False，队列将引发Empty异常
                val_even = self.data.get(1,5)  #get(self, block=True, timeout=None) ,1就是阻塞等待,5是超时5秒
                if val_even%2==0:
                    print "%s: %s is consuming. %d in the queue is consumed!" % (time.ctime(),self.getName(),val_even)
                    time.sleep(2)
                else:
                    self.data.put(val_even)
                    time.sleep(2)
            except:     #等待输入，超过5秒  就报异常
                print "%s: %s finished!" %(time.ctime(),self.getName())
                break

class Consumer_odd(threading.Thread):
    def __init__(self,t_name,queue):
        threading.Thread.__init__(self, name=t_name)
        self.data=queue
    def run(self):
        while 1:
            try:
                val_odd = self.data.get(1,5)
                if val_odd%2!=0:
                    print "%s: %s is consuming. %d in the queue is consumed!" % (time.ctime(), self.getName(), val_odd)
                    time.sleep(2)
                else:
                    self.data.put(val_odd)
                    time.sleep(2)
            except:
                print "%s: %s finished!" % (time.ctime(), self.getName())
                break
#Main thread
def main():
    queue = Queue()  #创建一个“队列”对象。可选参数maxsize来设定队列长度，如果maxsize小于1就表示队列长度无限
    '''
    Python Queue模块有三种队列及构造函数:
    FIFO队列先进先出。 class Queue.Queue(maxsize)
    LIFO类似于堆，即先进后出。 class Queue.LifoQueue(maxsize)
    还有一种是优先级队列级别越低越先出来。 class Queue.PriorityQueue(maxsize)

    常用队列操作方法(q = Queue.Queue()):
    q.qsize() 返回队列的大小
    q.empty() 如果队列为空，返回True,反之False
    q.full() 如果队列满了，返回True,反之False
    q.full 与 maxsize 大小对应
    q.get([block[, timeout]]) 获取队列，timeout等待时间
    q.get_nowait() 相当q.get(False)
    非阻塞 q.put(item) 写入队列，timeout等待时间
    q.put_nowait(item) 相当q.put(item, False)
    q.task_done() 在完成一项工作之后，q.task_done() 函数向任务已经完成的队列发送一个信号
    q.join() 实际上意味着等到队列为空，再执行别的操作
    '''

    producer = Producer('Pro.', queue)
    consumer_even = Consumer_even('Con_even.', queue)
    consumer_odd = Consumer_odd('Con_odd.',queue)
    consumer_even.start()
    consumer_odd.start()
    producer.start()
    producer.join()
    consumer_even.join()
    consumer_odd.join()
    print 'All threads terminate!'

if __name__ == '__main__':
    main()
