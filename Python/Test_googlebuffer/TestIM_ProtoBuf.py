#coding=utf8
from googlebufff import testim_pb_pb2
import sys
import json
from protobuf_to_dict import protobuf_to_dict, dict_to_protobuf

def login_proxy_body_serialize(im_account, auth_code, im_uid, proxy_topic):
    protobuf_login_proxy = testim_pb_pb2.login_proxy()

    protobuf_login_proxy.im_account = im_account
    protobuf_login_proxy.auth_code = auth_code
    protobuf_login_proxy.im_uid = im_uid
    if("" != proxy_topic):
        protobuf_login_proxy.proxy_topic = proxy_topic

    #序列化的
    login_proxy_body = protobuf_login_proxy.SerializeToString()
    #n = len(login_proxy_body)

    return login_proxy_body


def login_proxy_body_unserialize(serialize_data):
    protobuf_login_proxy = testim_pb_pb2.login_proxy()

    #反序列化
    protobuf_login_proxy.ParseFromString(serialize_data)

    print type(protobuf_login_proxy)
    print protobuf_login_proxy








def login_proxy_body_serialize2(datadic):
    #序列化的
    datapb = (dict_to_protobuf(getattr(testim_pb_pb2, 'login_proxy'), datadic)).SerializeToString()
    return datapb


def login_proxy_body_unserialize2(serialize_data):
    protobuf_login_proxy = testim_pb_pb2.login_proxy()

    #反序列化
    protobuf_login_proxy.ParseFromString(serialize_data)
    res = protobuf_to_dict(protobuf_login_proxy)

    print type(res)
    print json.dumps(res).decode('unicode_escape')





if __name__ == '__main__':
    # login_proxy_body = login_proxy_body_serialize("12321", '123', 12,'1234')
    # login_proxy_body_unserialize(login_proxy_body)

    datadic = {'im_account':'12321', 'auth_code':'123', 'im_uid':12, 'proxy_topic':'1234'}
    login_proxy_body = login_proxy_body_serialize2(datadic)
    login_proxy_body_unserialize2(login_proxy_body)

