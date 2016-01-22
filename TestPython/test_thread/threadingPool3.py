#coding=utf8
import threadpool
import time
import urllib2

urls = [
    'http://www.163.com',
    'http://www.amazon.com',
    'http://www.ebay.com',
    'http://www.alibaba.com',
    'http://www.reddit.com'
]

def myRequest(url):
    resp = urllib2.urlopen(url)
    print url, resp.getcode()


def timeCost(request, n):
  print "Elapsed time: %s" % (time.time()-start)

start = time.time()
pool = threadpool.ThreadPool(5)    #ThreadPool(poolsize)  表示最多可以创建poolsize这么多线程
reqs = threadpool.makeRequests(myRequest, urls, timeCost)   #makeRequests(some_callable, list_of_args, callback)
[ pool.putRequest(req) for req in reqs ]
pool.wait()
