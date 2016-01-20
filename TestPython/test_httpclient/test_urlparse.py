#coding=utf8
import urlparse


#将 urlstr 解析成一个 6-元组(prot_sch, net_loc,path, params, query,frag)
result = urlparse.urlparse('http://www.python.org/doc/FAQ.html')
print result

#反解析
urlstr = urlparse.urlunparse(result)
print urlstr


#urljoin()取得baseurl， 并将其基路径与newurl连接起来
urlstrj = urlparse.urljoin('http://www.python.org/doc/FAQ.html', 'current/lib/lib.htm')
print urlstrj
