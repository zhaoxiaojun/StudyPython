#coding=UTF8
'''
CGIHTTPServer 包含处理POST请求和执行CGICGIHTTPRequestHandler类
'''
import BaseHTTPServer
import CGIHTTPServer

HOST = ''
PORT = 8000

# Create the server, CGIHTTPRequestHandler is pre-defined handler
server = BaseHTTPServer.HTTPServer((HOST, PORT), CGIHTTPServer.CGIHTTPRequestHandler)
# Start the server
server.serve_forever()
