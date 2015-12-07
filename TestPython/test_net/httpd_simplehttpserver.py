#coding=UTF8
'''
SimpleHTTPServer 包含执行GET和HEAD请求的SimpleHTTPRequestHandler类
python自带了一个web服务器SimpleHTTPServer。我们可以很简单地输入下面的命令来启动web服务器，提供一个文件浏览的web服务。
python -m SimpleHTTPServer 80 然后在浏览器输入http://localhost  就可以看到当前目录下的所有目录和文件了。
'''
import SimpleHTTPServer
import SocketServer

HOST = ''
PORT = 8008

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer((HOST, PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()

