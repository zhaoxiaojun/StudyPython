#coding=utf8
__author__ = 'Dell'

import time
import pika
import struct
import random
import UBAS_niiwoo_pb2


MSG_OFFSET_HEADTAG='1'

MSG_OFFSET_FUNC_CODE=500006
MSG_OFFSET_BIG=0
MSG_OFFSET_SMALL=0
MSG_OFFSET_ENCRYPT='1'
MSG_OFFSET_SESSION_ID= 2015070 + random.Random().randint(1,9)
MSG_OFFSET_TO_ID=10006
MSG_OFFSET_FROM_ID=10001
MSG_OFFSET_APP_ID=10
MSG_OFFSET_RESERVER_FIELD1=10
MSG_OFFSET_RESERVER_FIELD2=10

MSG_CRC_CHECK = 18


ask = UBAS_niiwoo_pb2.niiwoo_UBAS_ask()
ans = UBAS_niiwoo_pb2.niiwoo_student_UBAS_ans()

ask.user_type = UBAS_niiwoo_pb2.en_user_student
ask.identity_card = '90988877666687811'
ask.real_name = '挨咬'
ask.mobile_phone = '12345789011'


MSG_OFFSET_BODY = ask.SerializeToString()
l = len(MSG_OFFSET_BODY)
MSG_OFFSET_DATA_LEN=l
MSG_OFFSET_PKT_LEN=48+l

print "MSG_OFFSET_BODY"
print l
print MSG_OFFSET_BODY

formt = "<ciihhcqiiiiii%dsh"%l
message=struct.pack(formt,MSG_OFFSET_HEADTAG,MSG_OFFSET_PKT_LEN,MSG_OFFSET_FUNC_CODE,MSG_OFFSET_BIG,MSG_OFFSET_SMALL,MSG_OFFSET_ENCRYPT,
										MSG_OFFSET_SESSION_ID,MSG_OFFSET_TO_ID,MSG_OFFSET_FROM_ID,
                    MSG_OFFSET_APP_ID,MSG_OFFSET_RESERVER_FIELD1,MSG_OFFSET_RESERVER_FIELD2,MSG_OFFSET_DATA_LEN,MSG_OFFSET_BODY,
                    MSG_CRC_CHECK)

#定义交换机

message = "message 00001"
print "message"
print len(message)
print message

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('192.168.18.77',5672,'pub',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='QDP_ANRONG', type='fanout')

channel.queue_declare(queue='QDP_ANRONG', durable=False)

body = message

channel.basic_publish(exchange='QDP_ANRONG',routing_key='',body=body)

print " [x] Sent %s" %body

time.sleep(1)
connection.close()
