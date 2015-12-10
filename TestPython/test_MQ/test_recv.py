#coding=utf8
import pika
import struct

#登录
credentials = pika.PlainCredentials('guest', 'guest')

#连接
parameters = pika.ConnectionParameters('192.168.18.77',5672,'pub',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

mq_queue = 'AFP_AFPFromQDP'

#定义交换机，设置类型为direct
channel.exchange_declare(exchange=mq_queue, type='fanout')
channel.queue_declare(queue=mq_queue)

#并绑定到交换机上，设置路由键
channel.queue_bind(exchange=mq_queue, queue=mq_queue, routing_key=mq_queue)

#拿到信息之后你要干麽?
def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    length= len(body)
    formt = "<ciihhcqiiiiii%dsi"%(length-50)
    msg=struct.unpack(formt, body)
    print msg
    print len(body)
    print msg[13]

#接收消息
channel.basic_consume(callback, queue=mq_queue, no_ack=True)  #no_ack=True是说，服务器你把消息发送出去之后就把那个信息从队列里删了吧。潜台词就是，可以不删除，然后其他消费者还可以取这条消息，怎样就不删除。no_ack=False,其实这个也是默认的

#让这个消费者一直在等待，只要有消息他就去取
print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()
