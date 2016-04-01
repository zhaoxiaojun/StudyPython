#coding=utf8
import stackless
import Queue
"""
生产者消费者
"""
queue = Queue.Queue()

def producer(i):
    global queue
    queue.put(i)
    print 'producer', i, 'add', i

def consumer():
    global queue
    i = queue.get()
    print 'consumer', i, 'get', i

for i in range(10):
    stackless.tasklet(producer)(i)

for i in range(10):
    stackless.tasklet(consumer)


stackless.run()



