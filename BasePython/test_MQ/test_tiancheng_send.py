#coding=utf8
import pika
import random
import time

#登录
credentials = pika.PlainCredentials('guest', 'guest')

#连接
parameters = pika.ConnectionParameters('192.168.18.84', 5672,'pub',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()


#消息数据
body = 'hello world'

#发送消息
exchangename = 'QDP_TONGDUN'
channel.basic_publish(exchange=exchangename, routing_key='', body=body)
print " Sent %s" % body


#关闭连接
channel.close()
connection.close()
print 'Sent end'
