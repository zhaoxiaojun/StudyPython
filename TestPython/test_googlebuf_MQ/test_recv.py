#coding=utf8
import pika
import struct
import threading
import thread
import time

class workk(threading.Thread):
    def __init__(self, tdname):
        threading.Thread.__init__(self, name=tdname)
        #登录
        credentials = pika.PlainCredentials('guest', 'guest')

        #连接
        parameters = pika.ConnectionParameters('192.168.18.77',5672,'pub',credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.mq_queue = 'TESTTEST'

        #mq_queue1 = 'TESTTEST1'

        #定义交换机
        #channel.exchange_declare(exchange=mq_queue, type='fanout')
        #channel.queue_declare(queue=mq_queue)

        #channel.exchange_declare(exchange=mq_queue1, type='fanout')
        #channel.queue_declare(queue=mq_queue1)

        #并绑定到交换机上，设置路由键
        #channel.queue_bind(exchange=mq_queue, queue=mq_queue)
        #channel.queue_bind(exchange=mq_queue1, queue=mq_queue1)

    #拿到信息之后你要干麽?
    def callback(self, ch, method, properties, body):
        print " [x] Received %r" % (body,)
        #length= len(body)
        #formt = "<ciihhcqiiiiii%dsi"%(length-50)
        #msg=struct.unpack(formt, body)
        #print msg
        print len(body)
        #print msg[13]

    def run(self):
        #接收消息
        self.channel.basic_consume(self.callback, queue=self.mq_queue, no_ack=True)
        #no_ack=True是说，服务器你把消息发送出去之后就把那个信息从队列里删了吧。潜台词就是，可以不删除，然后其他消费者还可以取这条消息，怎样就不删除，no_ack=False，其实这个也是默认的
        #channel.basic_consume(callback, queue=mq_queue1, no_ack=True)


        #让这个消费者一直在等待，只要有消息他就去取
        print '\n[*] Waiting for messages. To exit press CTRL+C'
        self.channel.start_consuming()
        print 1010101


workkthO = workk('workk')
#workkthO.setDaemon(True)
workkthO.start()

print 1111
print workkthO.isAlive()
workkthO.connection.close()
print workkthO.isAlive()
time.sleep(5)
print 2222
