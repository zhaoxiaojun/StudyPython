#coding=utf8

'''
WSGI：Web Server Gateway Interface
WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。
'''



def application(environ, start_response):
    '''
    application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
    environ：一个包含所有HTTP请求信息的dict对象；
    start_response：一个发送HTTP响应的函数。
    '''
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    print 'method:', method
    print 'path:', path
    start_response('200 OK', [('Content-Type', 'text/html')])    #只能调用一次start_response()函数。接收两个参数，一个是HTTP响应码一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

