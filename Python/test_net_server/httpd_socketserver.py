#coding=UTF8
from SocketServer import TCPServer, StreamRequestHandler, BaseRequestHandler
#SocketServer模块提供的请求处理类有BaseRequestHandler，以及它的派生类StreamRequestHandler和DatagramRequestHandler

host = ''
port = 21567
addr = (host, port)

class MyTCPHandler1(BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

class MyTCPHandler2(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from ',addr
        self.wfile.write('Thank you for connecting\n\n')

        self.data = self.rfile.readline().strip()
        print self.data
        print "{} wrote:".format(self.client_address[0])
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    # Create the server, binding to localhost on port 9999
    #实例化服务类对象
    server = TCPServer(addr, MyTCPHandler2)

    # Activate the server; this will keep running until you interrupt the program with Ctrl-C
    #开启服务
    server.serve_forever()


'''
        def handle(self):
            #客户端ip和port
            print 'got connection from ',self.request.getpeername()
            #print 'got connection from ',self.client_address

            #客户端请求数据
            print 'client request data:\n',self.request.recv(1024)
            #print 'client request data:\n',self.rfile.readline()

            #发送响应
            self.request.sendall('connection %s:%s at %s succeed!\n' % (host,port,ctime()))
            self.request.sendall('Thank you for connecting\n')
            #self.wfile.write('connection %s:%s at %s succeed!\n' % (host,port,ctime()))
            #self.wfile.write('Thank you for connecting\n')
'''
