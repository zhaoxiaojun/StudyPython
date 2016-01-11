#coding=utf8
import pika
import struct
import threading

class UPSMQ_Thread(threading.Thread):
    '''
    线程类
    '''
    def __init__(self, func, mq_queue, messages):
        threading.Thread.__init__(self)
        self.func = func
        self.mq_queue = mq_queue
        self.messages = messages

    def run(self):
        print "send to: %s messages: %s" % (self.mq_queue, self.messages)
        response = self.func(self.mq_queue, self.messages)
        print "response: %s" % response


class UPSMQ_Test(object):
    '''
    用户画像MQ接口测试类
    '''
    def __init__(self, username, passwd, MQhost, MQport, vhost):
        '''
        登录MQ建立连接
        '''
        credentials = pika.PlainCredentials(username, passwd)           #登录
        parameters = pika.ConnectionParameters(MQhost, MQport,vhost,credentials)          #连接
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)  #定义接收返回消息的队列
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.recv_response, no_ack=True, queue=self.callback_queue)  #订阅

    def recv_response(self, ch, method, props, body):
        '''
        返回消息处理
        '''
        self.response = body

    def request(self, mq_queue, messages):
        self.response = None
        self.channel.basic_publish(exchange = mq_queue,
                                    routing_key = '',
                                    properties = pika.BasicProperties(reply_to = self.callback_queue),
                                    body = messages)
        while self.response is None:                  #接收返回的数据
            self.connection.process_data_events()
        return self.response


def UPSMQ_PCTest(self, num):
    '''
    用户画像MQ接口并发压力测试
    '''
    #测试环境
    username = 'guest'
    passwd = 'guest'
    MQhost = '192.168.18.77'
    MQport = 5672
    vhost = 'pub'

    threads = []
    mq_queue = '_UBAS_DATA_ANALYSIS'
    messages = '123456abc'
    for n in num:
        UPSMQ_TestO = UPSMQ_Test(username, passwd, MQhost, MQport, vhost)
        threads.append(UPSMQ_Thread(UPSMQ_TestO.request, mq_queue, messages)

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    UPSMQ_PCTest(1)
