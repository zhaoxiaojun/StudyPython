#coding=utf8
"""
WSGI不是服务器，不是API，不是Python模块，更不是什么框架，而是一种服务器和客户端交互的接口规范PEP333！
"""


from wsgiref.simple_server import make_server
import hello

#创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8800, hello.application)
print('Serving HTTP on port 8800...')
# 开始监听HTTP请求:
httpd.serve_forever()
