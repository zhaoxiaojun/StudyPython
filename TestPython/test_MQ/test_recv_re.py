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


#声明消息队列
queuename = 'testing_re'
channel.queue_declare(queue=queuename, durable=False)



#定义回调函数---拿到信息之后干啥
def callback(ch, method, props, body):
    print "Received ch: %r" % ch
    print "Received body: %r" % body
    print "Received props: %r" % props
    print "Received method: %r\n" % method
    print "method.routing_key: %r" % method.routing_key
    print "method.redelivered: %r" % method.redelivered
    print "method.exchange: %r" % method.exchange
    print "method.delivery_tag: %r" % method.delivery_tag    #投递模式
    print "method.consumer_tag: %r\n" % method.consumer_tag
    print "props.reply_to: %r" % props.reply_to
    print "props.correlation_id: %r" %  props.correlation_id
    print "\n"

    #给发送者回消息，表示接收成功
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = props.correlation_id),
                     body='SUCESS!')
    #ch.basic_ack(delivery_tag = method.delivery_tag)

#接收消息
#channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue=queuename)

#让这个消费者一直在等待，只要有消息他就去取
print '\nWaiting for messages'
channel.start_consuming()
