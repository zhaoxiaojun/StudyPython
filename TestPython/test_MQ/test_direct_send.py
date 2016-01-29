#coding=utf8
import pika
import random
import time

#登录
credentials = pika.PlainCredentials('guest', 'guest')

#连接
parameters = pika.ConnectionParameters('192.168.18.77', 5672,'pub',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()


#消息数据
body = 'hello world'

#发送消息: exchange表示交换器 routing_key表示路由键  body就是发送的内容
exchangename = 'testing_exd'
channel.basic_publish(exchange=exchangename, routing_key='info', body=body)
print " Sent %s" % body


#关闭连接
channel.close()
connection.close()
print 'Sent end'
