







#coding=utf8
#import googlebufff
#import testim_pb_pb2
#反序列化
#序列化
from googlebufff import testim_pb_pb2
login_proxy_body = protobuf_login_proxy.SerializeToString()
n = len(login_proxy_body)
print  protobuf_login_proxyf
print  type(protobuf_login_proxyf)
print 'login_proxy_body:', login_proxy_body
print 'n: ', n
protobuf_login_proxy = testim_pb_pb2.login_proxy()
protobuf_login_proxy.auth_code = 'auth_code'
protobuf_login_proxy.im_account = 'im_account'
protobuf_login_proxy.im_uid = 1
protobuf_login_proxy.proxy_topic = 'proxy_topic'
protobuf_login_proxyf = testim_pb_pb2.login_proxy()
protobuf_login_proxyf.ParseFromString(login_proxy_body)
