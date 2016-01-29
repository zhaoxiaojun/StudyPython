#coding=utf8
import pika
import random
import time
import CustomDataPg
import GoogleProtoBuffer

#登录
credentials = pika.PlainCredentials('guest', 'guest')

#连接
parameters = pika.ConnectionParameters('192.168.18.84',5672,'pub',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

#声明fanout类型的交换机: 转发消息到所有绑定队列
exchangename = 'QDP_TONGDUN'
#channel.exchange_declare(exchange=exchangename, type='fanout')


#声明消息队列
#消费者自己声明队列
queuename = exchangename + '_ttt'
channel.queue_declare(queue=queuename, durable=False)


#将自己声明队列绑定到交换机上
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
    print "method.consumer_tag: %r\n" % method.consumer_tag
    print "dir(properties): %r" % dir(properties)
    print "dir(method): %r" % dir(method)
    print "dir(ch): %r" % dir(ch)
    print "\n--------------------------------------------------"

    PketO = CustomDataPg.ProtoPket()
    ProBufO = GoogleProtoBuffer.ProBuffer()
    #解析body
    funcode, pdata = PketO.unpackPket(body)
    print  'funcode: ', funcode
    print 'pdata: ', pdata
    response_topic, mobile_phone, ip, mac, imei = ProBufO.Unserialize(pdata)
    print 'response_topic: ', response_topic
    print 'mobile_phone: ', mobile_phone
    print 'ip: ', ip
    print 'mac: ', mac
    print 'imei: ', imei

    #构造body
    print '\n--------------'
    MQMockDatai = '{"score": "950"}'
    pbdata = ProBufO.Serialize(MQMockDatai)
    print 'pbdata: ', pbdata
    resp_body = PketO.packPket(pbdata, funcode)
    print 'resp_body: ',resp_body

    #测试还原
    print '\n--------------'
    funcodet, pdatat = PketO.unpackPket(resp_body)
    json_ans = ProBufO.testUnSerialize(pdatat)

    print 'funcodet: ', funcodet
    print 'json_ans: ',json_ans

    #发送
    ch.basic_publish(exchange=response_topic,
                    routing_key='',
                    body=resp_body)
    print 'Send to: [exchange]response_topic: %s end!' % response_topic



#接收消息
channel.basic_consume(callback, queue=queuename, no_ack=True)

#让这个消费者一直在等待，只要有消息他就去取
print '\nWaiting for messages'
channel.start_consuming()

