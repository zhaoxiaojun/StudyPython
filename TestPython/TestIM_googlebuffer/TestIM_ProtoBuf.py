#coding=utf8
#from googlebufff import testim_pb_pb2
import googlebufff
import sys

def login_proxy_body_serialize(im_account, auth_code, im_uid, proxy_topic):
    protobuf_login_proxy = googlebufff.testim_pb_pb2.login_proxy()

    protobuf_login_proxy.im_account = im_account
    protobuf_login_proxy.auth_code = auth_code
    protobuf_login_proxy.im_uid = im_uid
    if("" != proxy_topic):
        protobuf_login_proxy.proxy_topic = proxy_topic

    #序列化的
    login_proxy_body = protobuf_login_proxy.SerializeToString()
    n = len(login_proxy_body)

    return login_proxy_body,n


def login_proxy_body_unserialize(serialize_data):
    protobuf_login_proxy = googlebufff.testim_pb_pb2.login_proxy()

    #反序列化
    protobuf_login_proxy.ParseFromString(serialize_data)

    return protobuf_login_proxy




#test----------------------------------------------------
yn_Body_serialize = ["0", "1"]  #序列化or反序列化
#参数检查
arglen = len(sys.argv)
if 2 > arglen:
    print "Uage: number of args is error!"
    sys.exit()

if yn_Body_serialize[0] == sys.argv[1]:
    if 6 != arglen:
        print "Uage: number of args is error!"
        sys.exit()
    im_account = sys.argv[2]
    auth_code = sys.argv[3]
    im_uid = int(sys.argv[4])
    proxy_topic = sys.argv[5]

    body_serialize = login_proxy_body_serialize(im_account, auth_code, im_uid, proxy_topic)[0]
    body_serialize_len = login_proxy_body_serialize(im_account, auth_code, im_uid, proxy_topic)[1]
    #写入文件
    f = open("D:\\CODE\\yzhPython\\test_protocbuf\\buftmpIM","wb")
    f.write(body_serialize)
    f.close()
    print body_serialize
    print body_serialize_len

elif yn_Body_serialize[1] == sys.argv[1]:
    if 2 != arglen:
        print "Uage: number of args is error!"
        sys.exit()

    #读文件中的序列化数据
    f = open("D:\\CODE\\yzhPython\\test_protocbuf\\buftmpIM","rb")
    body_serialize = f.read()
    f.close()
    #body_serialize = sys.argv[2]

    body = login_proxy_body_unserialize(body_serialize)
    print body

else:
    print sys.argv[1]
    print "Uage: argv[1] is error!"
    sys.exit()



