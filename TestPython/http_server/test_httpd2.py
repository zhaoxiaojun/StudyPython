#coding=UTF8
from SocketServer import TCPServer, StreamRequestHandler, BaseRequestHandler
host = ''
port = 21567
addr = (host, port)

class MyTCPHandler1(BaseRequestHandler):
    def __init__(self, data):
        BaseRequestHandler.__init__(self)
        self.data = data

    def handle(self):
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

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    #开启服务
    server.serve_forever()
