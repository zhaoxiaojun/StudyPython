#coding=utf8
import pika
import random

#登录
credentials = pika.PlainCredentials('guest', 'guest')

#连接
parameters = pika.ConnectionParameters('192.168.18.77', 5672,'pub',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

mq_queue = 'TESTTEST1'
mq_exchange = 'TESTTEST1'
#mq_queue1 = 'TESTTEST1'

#声明交换机
channel.exchange_declare(exchange=mq_exchange, type='fanout')
#channel.exchange_declare(exchange=mq_queue1, type='fanout')

#声明消息队列(durable非持久)  如果没有就创建 不会重复创建
channel.queue_declare(queue=mq_queue, durable=False)
#channel.queue_declare(queue=mq_queue1, durable=False)

#构造数据
number = random.randint(1,1000)
body = 'hello world:%s' %number

#发送消息到队列，其中exchange表示交换器，能精确指定消息应该发送到哪个队列，routing_key设置为队列的名称，body就是发送的内容
channel.basic_publish(exchange=mq_exchange, routing_key=mq_queue, body=body)
print " [x] Sent %s" %body

"""
#构造数据
number = random.randint(1,1000)
body = 'hello world:%s' %number

#发送消息到队列，其中exchange表示交换器，能精确指定消息应该发送到哪个队列，routing_key设置为队列的名称，body就是发送的内容
channel.basic_publish(exchange=mq_queue1, routing_key='', body=body)
print " [x] Sent %s" %body
"""
#关闭连接
connection.close()
