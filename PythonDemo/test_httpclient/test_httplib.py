#coding=utf8
import urllib
import httplib
'''
httplib是一个相对底层的http请求模块，其上有专门的包装模块，如urllib内建模块
参考官网: http://docs.python.org/library/httplib.html
'''

'''
原型： HTTPConnection(host[, port[, strict[, timeout]]])
功能: 该类用于创建一个http类型的请求链接 (返回一个HTTPConnection对象)
host: 请求的服务器host，不能带http://开头
port: 服务器web服务端口
strict: 是否严格检查请求的状态行，就是http1.0/1.1 协议版本的那一行，即请求的第一行，默认为False，为True时检查错误会抛异常
timeout: 单次请求的超时时间，没有时默认使用httplib模块内的全局的超时时间
'''
#conn1 = HTTPConnection('www.baidu.com:80')
#conn2 = HTTPconnection('www.baidu.com',80)
#conn3 = httplib.HTTPConnection('www.baidu.com',80,True,10)
conn3 = httplib.HTTPConnection('192.168.11.250',5556)

'''
原型：HTTPSConnection(host[, port[, key_file[, cert_file[, strict[, timeout]]]]])
功能：该类用于创建一个https类型的请求链接 (返回一个HTTPSConnection对象)
key_file:一个包含PEM格式的私钥文件
cert_file:一个包含PEM格式的认证文件
other：其它同http参数
'''
#conn3 = HTTPSConnection('accounts.google.com',443,key_file,cert_file,True,10)


'''
原型： conn.request(method, url[, body[, headers]])
功能：发送一个请求(无返回，其实就是相对于向服务其发送数据，但是没有最后回车)
method: 请求的方式，如'GET','POST','HEAD','PUT','DELETE'等
url: 请求的网页路径。如：'/index.html'
body: 请求是否带数据，该参数是一个字典
headers: 请求是否带头信息，该参数是一个字典，不过键的名字是指定的http头关键字
'''
conn3.request('QUIT', '/', '', {'user-agent':'test'})


'''
获取一个http响应对象，相当于执行最后的2个回车(返回HTTPResponse对象)
'''
#res = conn3.getresponse()

'''
关闭指定的httpconnect链接
'''
conn3.close()
print 'end'
"""

'''
原型：body = res.read([amt])
功能：获得http响应的内容部分，即网页源码（返回网页内容字符串）
amt: 读取指定长度的字符，默认为空，即读取所有内容
'''
body = res.read()
pbody = res.read(10)

headers = res.getheaders()  #获得所有的响应头内容，是一个元组列表[(name,value),(name2,value2)]
header = res.getheader(name)  #getheader(name[,default])  获得name指定的头内容
fileno = res.fileno()   #socket的fileno

print res.msg    #所有的头信息，和getheaders方法一样，只不过这个是原始未处理的字符串
print res.status   #当次请求的状态
print res.version  #当次请求的http协议版本，10是http1.0, 11是http/1.1
print res.reason   #当次请求的结果的表述内容，200是ok，404是Not Found



def sendhttp():
    data = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
    headers = {"Content-type": "application/x-www-form-urlencoded",
                "Accept": "text/plain"}
    conn = httplib.HTTPConnection('bugs.python.org')
    conn.request('POST', '/', data, headers)
    httpres = conn.getresponse()
    print httpres.status
    print httpres.reason
    print httpres.read()

if __name__ == '__main__':
    sendhttp()

"""
