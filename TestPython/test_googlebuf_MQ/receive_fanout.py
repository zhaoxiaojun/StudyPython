#!/usr/bin/env python
#coding=utf8
import pika
import logging
logging.basicConfig()

credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.18.41', 5672, 'pub', credentials))
channel = connection.channel()

#定义交换机
channel.exchange_declare(exchange='test_fanout', type='fanout')
 
#随机生成队列，并绑定到交换机上
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

print("queue_name: %s" % queue_name)
channel.queue_bind(exchange='test_fanout', queue=queue_name)
 
def callback(ch, method, properties, body):
    print " [x] Received %r %r" % (method.routing_key, body,)
 
channel.basic_consume(callback, queue=queue_name, no_ack=True)
 
print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()

