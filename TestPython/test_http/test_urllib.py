#coding=utf8
import urllib


url = 'http://www.51testing.com/html/index.html'
resp = urllib.urlopen(url)
'''
发送请求：
GET /html/index.html HTTP/1.0
Host: www.51testing.com
User-Agent: Python-urllib/1.17
'''
page = resp.read()
#print page
#print dir(resp)
print '\n--------------------------------------\n'


data = 'abcdsdfsdf'
resp = urllib.urlopen(url, data)
'''
发送请求：
POST /html/index.html HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 10
Host: www.51testing.com
User-Agent: Python-urllib/1.17

abcdsdfsdf
'''
page = resp.read()
f = open('./urllib_index.html', 'w')
f.write(page)
print '\n--------------------------------------\n'




'''
urllib.urlretrieve(url, local_name, method)
直接把url链接网页内容下载到retrieve_index.html里了，适用于单纯的下载的功能。
'''
url = 'http://www.douban.com/'
urllib.urlretrieve(url, './retrieve_index.html')
print '\n--------------------------------------\n'



'''
编码
'''
s = urllib.quote('This is python')  #编码
print 'quote:\t'+s    #空格用%20替代

s_un = urllib.unquote(s)    #解码
print 'unquote:\t'+s_un

s_plus = urllib.quote_plus('This is python')  #编码
print 'quote_plus:\t'+s_plus            #空格用＋替代

s_unplus = urllib.unquote_plus(s_plus)       #解码
print 's_unplus:\t'+s_unplus

s_dict = {'name': 'dkf', 'pass': '1234'}
s_encode = urllib.urlencode(s_dict)    #编码字典转换成url参数
print 's_encode:\t'+s_encode
