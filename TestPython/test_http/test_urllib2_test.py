#coding=utf8
import urllib2


#重定向 urllib2默认情况下会针对3xx HTTP返回码自动进行Redirect动作无需人工配置
response =urllib2.urlopen('http://www.google.cn')
whether_redirected = response.geturl() == 'http://www.google.cn'


#不适用自动重定向 控制重定向
class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        pass
opener =urllib2.build_opener(RedirectHandler)
opener.open('http://www.google.cn')


#HTTP的PUT和DELETE方法
request = urllib2.Request(uri, data=data)
request.get_method = lambda: 'PUT'     # or 'DELETE'
response = urllib2.urlopen(request)


#Debug Log打开
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.google.com')
