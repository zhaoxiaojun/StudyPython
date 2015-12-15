#coding=utf8
from gevent import monkey; monkey.patch_socket()
import gevent
import urllib2


def f(n):
    for i in range(n):
        print gevent.getcurrent(), i
        gevent.sleep(0)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()
print '\n--------------------------------\n'


def f(url):
    print('GET: %s' % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(f, 'http://www.baidu.com/'),
        gevent.spawn(f, 'http://www.163.com/'),
        gevent.spawn(f, 'http://www.51testing.com/'),
])
#3个网络操作是并发执行的，结束顺序不同，但只有一个线程。
#由于gevent是基于IO切换的协程，所以最神奇的是，我们编写的Web App代码，不需要引入gevent的包，也不需要改任何代码，仅仅在部署的时候，用一个支持gevent的WSGI服务器，
#立刻就获得了数倍的性能提升
