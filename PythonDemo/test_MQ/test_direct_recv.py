#coding=utf8
import pika
import random
import time

#登录
credentials = pika.PlainCredentials('guest', 'guest')

#连接
parameters = pika.ConnectionParameters('192.168.18.77',5672,'pub',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

#声明direct类型的交换机
'''
处理路由键, 需要将一个队列绑定到交换机上，要求该消息与一个特定的路由键完全匹配。这是一个完整的匹配。如果一个队列绑定到该交换机上要求路由键"dog"，则只有被标
记为"dog"的消息才被转发
'''
exchangename = 'testing_exd'
channel.exchange_declare(exchange=exchangename, type='direct')


#声明消息队列： durable：是否是坚固的---具有这个标志的队列和交换机会在重启之后重新建立（不表示说在队列当中的消息会在重启后恢复）
queuename = 'testing_qud'
channel.queue_declare(queue=queuename, durable=False)


#将队列绑定到交换机上并设置路由键
routings = ['debug','info','error']
for routing in routings:
    channel.queue_bind(exchange = exchangename,
                        queue = queuename,
                        routing_key = routing)


#定义回调函数---拿到信息之后干啥
def callback(ch, method, properties, body):
    print "Received ch: %r" % ch
    print "Received body: %r" % body
    print "Received properties: %r" % properties
    print "Received method: %r\n" % method
    print "method.routing_key: %r" % method.routing_key
    print "method.redelivered: %r" % method.redelivered
    print "method.exchange: %r" % method.exchange
    print "method.delivery_tag: %r" % method.delivery_tag #投递模式
    print "method.consumer_tag: %r" % method.consumer_tag
    print "\n"

#接收消息
channel.basic_consume(callback, queue=queuename, no_ack=True)
'''
no_ack=True
是说服务器你把消息发送出去之后就把那个信息从队列里删了吧
no_ack=False
默认的,服务器你把消息发送出去之后不删除队列里的队列里，然后其他消费者还可以取这条消息
'''

#让这个消费者一直在等待，只要有消息他就去取
print '\nWaiting for messages'
channel.start_consuming()

