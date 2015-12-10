#coding=utf8
import urllib2
'''
提供一些复杂的接口用于处理： 基本认证，重定向，Cookies等
'''
　
'''
原型：urllib2.build_opener([handler, ...])
参数handler是Handler实例，常用的有HTTPBasicAuthHandler、HTTPCookieProcessor、ProxyHandler等。build_opener()返回的对象具有open()方法，与urlopen()函数的功能相同。
'''
#修改http报头
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
response = opener.open('http://www.example.com/')
print response.read()
print '\n--------------------------------------\n'


#密码验证： HTTPBasicAuthHandler
auth = urllib2.HTTPBasicAuthHandler()
auth.add_password('Administrator','http://www.example.com','Dave','123456')
#原型：add_password(realm,uri,user,passwd)
#realm是与验证相关联的名称或描述信息，取决于远程服务器。uri是基URL。user和passwd分别指定用户名和密码
opener = urllib2.build_opener(auth)
u = opener.open('http://www.example.com/evilplan.html')
print u.read()
print '\n--------------------------------------\n'


password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://www.163.com/"
password_mgr.add_password(None, top_level_url, username, password)
handler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(handler)
#urllib2.install_opener(opener)
u = opener.open('http://www.example.com/evilplan.html')
print u.read()
print '\n--------------------------------------\n'


#Cookie处理： HTTPCookieProcessor
cookie = cookielib.CookieJar()   #在内存中加载cookie
#cookie = cookielib.LWPCookieJar() #在硬盘中存储cookie
cookiehand = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(cookiehand)
u = opener.open('http://www.example.com/evilplan.html')
print u.read()
print '\n--------------------------------------\n'


#代理： ProxyHandler
proxy = ProxyHandler({'http':'http://someproxy.com:8080'}) #参数是一个字典，将协议名称（http，ftp）等映射到相应代理服务器的URL
auth = HTTPBasicAuthHandler()
auth.add_password()
opener = build_opener(auth,proxy)
u = opener.open('http://www.example.com/evilplan.html')
print u.read()
print '\n--------------------------------------\n'

#使用代理方法2：
proxy = 'http://%s:%s@%s' % ('userName', 'password', 'proxy')
inforMation = urllib2.urlopen("http://www.example.com", proxies={'http':proxy})


#明确控制Proxy:
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http": 'http://some-proxy.com:8080'})
null_proxy_handler =urllib2.ProxyHandler({})
if enable_proxy:
    opener =urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)



'''
原型：urllib2.install_opener(opener)
安装不同的opener对象作为urlopen()使用的全局opener
'''
req = urllib2.Request('http://www.51testing.com/html/index.html')
opener = urllib2.build_opener()       #创建opener对象
urllib2.install_opener(opener)     #定义全局默认opener
f = urllib2.urlopen(req)          #urlopen使用默认opener，但是install_opener已经把opener设为全局默认了，这里便是使用上面的建立的opener
page = f.read()
print page

