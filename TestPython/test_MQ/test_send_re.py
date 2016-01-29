#coding=utf8
import pika
import random
import time
import uuid

#登录
credentials = pika.PlainCredentials('guest', 'guest')

#连接
parameters = pika.ConnectionParameters('192.168.18.77', 5672,'pub',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

#消息数据
body = 'hello world'

#定义接收返回消息的队列
result = channel.queue_declare(exclusive=True)
callback_queue = result.method.queue

#定义接收返回消息的回调函数
def on_response(ch, method, props, body):
    print 'response body: ', body
    print 'correlation id: ', props.correlation_id

#订阅
channel.basic_consume(on_response,
                        no_ack=True,
                        queue=callback_queue)


#发送消息
queuename = 'testing_re'
corr_id = str(uuid.uuid4())
print 'genener corr_id: ', corr_id
channel.basic_publish(exchange='',
                        routing_key=queuename,
                        properties=pika.BasicProperties(
                            reply_to=callback_queue,
                            correlation_id=corr_id,   #关联ID
                        ),
                        body=body)
print " Sent %s" % body


#让这个消费者一直在等待，只要有消息他就去取
print '\nWaiting for response'
#channel.start_consuming()
time.sleep(3)
connection.process_data_events()

#关闭连接
channel.close()
connection.close()
print 'Sent end'
