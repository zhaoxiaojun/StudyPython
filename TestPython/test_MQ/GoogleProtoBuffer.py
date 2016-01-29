#coding=utf8
#######################################################
#filename: GoogleProtoBuffer.py
#author: defias
#date: 2016-1
#function: google proto buffer
#######################################################
from GoogleProtoBufPb2 import QDP_main_frame_pb2
from GoogleProtoBufPb2 import common_pb2

class ProBuffer(object):
    '''
    google buffer数据协议
    '''
    def __init__(self):
        pass

    def Unserialize(self, data):
        '''
        反序列化 获得:response_topic  mobile_phone ip mac imei
        '''
        user_verification_ask = QDP_main_frame_pb2.user_verification_ask()
        user_verification_ask.ParseFromString(data)
        response_topic = user_verification_ask.ask_header.response_topic
        mobile_phone = user_verification_ask.info.mobile_phone
        ip = user_verification_ask.ip
        mac = user_verification_ask.mac
        imei = user_verification_ask.imei

        return response_topic, mobile_phone, ip, mac, imei

    def Serialize(self, data):
        '''
        序列化
        '''
        user_verification_ans = QDP_main_frame_pb2.user_verification_ans()
        user_verification_ans.platform_type = QDP_main_frame_pb2.fraud_metrix
        user_verification_ans.error.error_code = common_pb2.ASK_SUCCEED
        user_verification_ans.json_ans = bytes(data)
        user_verification_ans_str = user_verification_ans.SerializeToString()

        return user_verification_ans_str

    def testUnSerialize(self, data):
        user_verification_ans = QDP_main_frame_pb2.user_verification_ans()
        user_verification_ans.ParseFromString(data)
        json_ans = user_verification_ans.json_ans
        return json_ans
