#coding=utf8
import httplib2
import urllib
import socks

h = httplib2.Http(".cache")
resp, content = h.request("http://example.org/", "GET")
print resp, content  #响应头和响应体
print '\n--------------------------------------\n'

#Authentication
h = httplib2.Http(".cache")
h.add_credentials('name', 'password')
resp, content = h.request("https://example.org/chap/2", "PUT",
    body="This is text",
    headers={'content-type':'text/plain'})
print resp, content


#Cache-Control
h = httplib2.Http(".cache")
resp, content = h.request("http://bitworking.org/")  #请求被缓存，下次还会用这个缓存而不去发送新的请求，缓存生效时间有web配置决定
#...
resp, content = h.request("http://bitworking.org/",
    headers={'cache-control':'no-cache'})   #设置不用缓存，当次将不用缓存，而是直接发一个新的请求

#Forms
h = httplib2.Http()
data = dict(name="Joe", comment="A test comment")
resp, content = h.request("http://bitworking.org/news/223/Meet-Ares", "POST", urllib.urlencode(data))



#Cookies
http = httplib2.Http()
url = 'http://www.example.com/login'
body = {'USERNAME': 'foo', 'PASSWORD': 'bar'}
headers = {'Content-type': 'application/x-www-form-urlencoded'}
response, content = http.request(url, 'POST', headers=headers, body=urllib.urlencode(body))

headers = {'Cookie': response['set-cookie']}   #获得cookie设置到请求头中以备下次请求使用
url = 'http://www.example.com/home'
response, content = http.request(url, 'GET', headers=headers)  #本次请求就不用带用户名密码了


#Proxies
httplib2.debuglevel=4
h = httplib2.Http(proxy_info = httplib2.ProxyInfo(socks.PROXY_TYPE_HTTP, 'localhost', 8000))
r,c = h.request("http://bitworking.org/news/")
