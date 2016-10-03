#coding=utf8
import testim_pb_pb2
import sys

def login_proxy_body_serialize(im_account, auth_code, im_uid, proxy_topic):
    protobuf_login_proxy = testim_pb_pb2.login_proxy()
  
    protobuf_login_proxy.im_account = im_account
    protobuf_login_proxy.auth_code = auth_code
    protobuf_login_proxy.im_uid = im_uid
    protobuf_login_proxy.proxy_topic = proxy_topic

    #序列化的
    login_proxy_body = protobuf_login_proxy.SerializeToString()
    return login_proxy_body

def login_proxy_body_serialize2(im_account, auth_code, im_uid):
    protobuf_login_proxy = testim_pb_pb2.login_proxy()
  
    protobuf_login_proxy.im_account = im_account
    protobuf_login_proxy.auth_code = auth_code
    protobuf_login_proxy.im_uid = im_uid

    #序列化的
    login_proxy_body = protobuf_login_proxy.SerializeToString()
    return login_proxy_body

def login_proxy_body_unserialize(filename):
    #"D:\\CODE\\CPP\\Test_TestIM_DLL_CMD\\Test_TestIM_DLL_CMD\\buftmpIM"
    #读文件中的序列化数据
    f = open(filename,"rb")
    serialize_data = f.read()
    f.close()
    
    #反序列化
    protobuf_login_proxy = testim_pb_pb2.login_proxy()
    protobuf_login_proxy.ParseFromString(serialize_data) 

    return protobuf_login_proxy




#test----------------------------------------------------
yn_Body_serialize = ["0", "1"]  #序列化or反序列化
#参数检查
arglen = len(sys.argv)
if 2 > arglen:
    #print "Uage: number of args is error!"
    sys.exit()
    
if yn_Body_serialize[0] == sys.argv[1]:
    if 5 > arglen:
        #print "Uage: number of args is error!"
        sys.exit()
    if 5 == arglen:
        im_account = sys.argv[2]
        auth_code = sys.argv[3]
        im_uid = int(sys.argv[4])
        body_serialize = login_proxy_body_serialize2(im_account, auth_code, im_uid)
        #写入文件
        #f = open("D:\\CODE\\CPP\\Test_TestIM_DLL_CMD\\Test_TestIM_DLL_CMD\\buftmpIM","wb")
        #f.write(body_serialize)
        #f.close()
        print body_serialize
    if 6 <= arglen:
        im_account = sys.argv[2]
        auth_code = sys.argv[3]
        im_uid = int(sys.argv[4])
        proxy_topic = sys.argv[5]
        body_serialize = login_proxy_body_serialize(im_account, auth_code, im_uid, proxy_topic)
        print body_serialize
    
elif yn_Body_serialize[1] == sys.argv[1]:
    if 3 > arglen:
        #print "Uage: number of args is error!"
        sys.exit()
    filename = sys.argv[2]
    body = login_proxy_body_unserialize(filename)
    print body
else:
    sys.exit()

    


