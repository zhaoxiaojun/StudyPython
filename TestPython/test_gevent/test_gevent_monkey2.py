#coding=utf8
from gevent import monkey
import gevent
import urllib2
monkey.patch_socket()

def f(url):
    print('GET: %s' % url)
    print gevent.getcurrent()         #3个网络操作是并发执行的，但只有一个线程
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(f, 'http://www.baidu.com/'),
        gevent.spawn(f, 'http://www.163.com/'),
        gevent.spawn(f, 'http://www.51testing.com/'),
])


