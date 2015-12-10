#coding=utf8
import urllib2
'''
urllib2可以接受一个Request对象，并以此可以来设置一个URL的headers，但是urllib只接收一个URL。这意味着，你不能伪装你的用户代理字符串等
urllib模块可以提供进行urlencode的方法，该方法用于GET查询字符串的生成，urllib2的不具有这样的功能。这就是urllib与urllib2经常在一起使用的原因
'''

#原型：urllib2.urlopen(url[, data][, timeout])
response = urllib2.urlopen('http://www.51testing.com/html/index.html')
'''
发送GET请求:
GET /html/index.html HTTP/1.1
Accept-Encoding: identity
Host: www.51testing.com
Connection: close
User-Agent: Python-urllib/2.7
'''
html = response.read()
url = response.geturl()  #返回检索的URL资源，这个是返回的真正url，通常是用来鉴定是否重定向的
info = response.info()  #返回页面的原信息就像一个字段的对象
code = response.getcode() #返回响应的HTTP状态代码
print 'html:', html
print 'url:', url
print 'info:', info
print 'code:', code
print '\n--------------------------------------\n'


response = urllib2.urlopen('http://www.51testing.com/html/index.html', timeout=1)
html = response.read()
print html
print '\n--------------------------------------\n'


#原型：class urllib2.Request(url[, data][, headers][, origin_req_host][, unverifiable])
req = urllib2.Request('http://www.51testing.com/html/index.html')
response = urllib2.urlopen(req)  #Request类是一个抽象的URL请求
'''
发送GET请求:
GET /html/index.html HTTP/1.1
Accept-Encoding: identity
Host: www.51testing.com
Connection: close
User-Agent: Python-urllib/2.7
'''
the_page = response.read()
#print the_page
print '\n--------------------------------------\n'


url = 'http://www.51testing.com/html/index.html'
values = {'name' : 'Michael Foord', 'location' : 'Northampton', 'language' : 'Python' }
data = urllib.urlencode(values)  #urlencode不能直接处理unicode对象，所以如果是unicode需要由unicode转到utf8
print data
req = urllib2.Request(url, data)  #如果没有data需要发送可以为None   当请求含有data参数时HTTP的请求为POST
#response = urllib2.urlopen(req)
'''
发送POST请求:
POST /html/index.html HTTP/1.1
Accept-Encoding: identity
Content-Length: 55
Host: www.51testing.com
Content-Type: application/x-www-form-urlencoded
Connection: close
User-Agent: Python-urllib/2.7

name=Michael+Foord&language=Python&location=Northampton
'''
the_page = response.read()
#print the_page
print '\n--------------------------------------\n'


#自定义http头
url = 'http://www.51testing.com/html/index.html'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'Michael Foord', 'location' : 'Northampton', 'language' : 'Python'}
headers = {'User-Agent' : user_agent, 'abcd':'abcd'}
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
#response = urllib2.urlopen(req)
'''
发送POST请求:
POST /html/index.html HTTP/1.1
Accept-Encoding: identity
Abcd: abcd
Content-Length: 55
Host: www.51testing.com
User-Agent: Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)
Connection: close
Content-Type: application/x-www-form-urlencoded

name=Michael+Foord&language=Python&location=Northampton
'''
the_page = response.read()
#print the_page
print '\n--------------------------------------\n'


#自定义http头方法二
req = urllib2.Request('http://www.51testing.com/html/index.html')
req.add_header('Referer', 'http://www.python.org/')
req.add_header('abcd', 'abcd')
#r = urllib2.urlopen(req)
'''
GET /html/index.html HTTP/1.1
Accept-Encoding: identity
Abcd: abcd
Host: www.51testing.com
Referer: http://www.python.org/
Connection: close
User-Agent: Python-urllib/2.7
'''
#the_page = r.read()
#print the_page
print '\n--------------------------------------\n'


'''
origin_req_host——是RFC2965定义的源交互的request-host。默认的取值是cookielib.request_host(self)。
这是由用户发起的原始请求的主机名或IP地址。例如，如果请求的是一个HTML文档中的图像，这应该是包含该图像的页面请求的request-host。

unverifiable ——代表请求是否是无法验证的，它也是由RFC2965定义的。默认值为false。
一个无法验证的请求是，其用户的URL没有足够的权限来被接受。例如，如果请求的是在HTML文档中的图像，但是用户没有自动抓取图像的权限，unverifiable的值就应该是true。
'''
