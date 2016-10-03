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

#声明fanout类型的交换机: 转发消息到所有绑定队列
'''
不处理路由键, 你只需要简单的将队列绑定到交换机上,一个发送到交换机的消息都会被转发到与该交换机绑定的所有队列上。很像子网广播，每台子网内的主机都获得了一份
复制的消息。Fanout交换机转发消息是最快的
'''
exchangename = 'testing_ex'
channel.exchange_declare(exchange=exchangename, type='fanout')


#声明消息队列： durable：是否是坚固的---具有这个标志的队列和交换机会在重启之后重新建立（不表示说在队列当中的消息会在重启后恢复）
queuename = 'testing_qu'
channel.queue_declare(queue=queuename, durable=False)


#将队列绑定到交换机上
channel.queue_bind(exchange=exchangename, queue=queuename)


#定义回调函数---拿到信息之后干啥
def callback(ch, method, properties, body):
    print "Received ch: %r" % ch
    print "Received body: %r" % body
    print "Received properties: %r" % properties
    print "Received method: %r\n" % method
    print "method.routing_key: %r" % method.routing_key
    print "method.redelivered: %r" % method.redelivered
    print "method.exchange: %r" % method.exchange
    print "method.delivery_tag: %r" % method.delivery_tag    #投递模式
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



'''
1、如果没有队列绑定在交换机上，则发送到该交换机上的消息会丢失
2、一个交换机可以绑定多个队列，一个队列可以被多个交换机绑定
3、临时队列: channel.queueDeclare()，有时不需要指定队列的名字，并希望断开连接时删除队列
'''

'''
如何使队列当中的消息在重启后恢复？
1、将交换机设成durable 　　
2、将队列设成durable
3、将消息的Delivery Mode 设置成2

不允许你绑定一个非坚固（non-durable）的交换机和一个durable的队列。反之亦然。要想成功必须队列和交换机都是durable的。 一旦创建了队列和交换机，
就不能修改其标志了。例如，如果创建了一个non-durable的队列，然后想把它改变成durable的，唯一的办法就是删除这个队列然后重现创建。
'''
