#coding=UTF8
import socket
import urllib
import json
RECV_LEN = 4096  #接收请求数据长度
MAX_CONN = 100   #最大连接数

#server code
class http_server():
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def set_header(self, header='''HTTP/1.1 200 ok\nContent-Type: text/html\n\n'''):
        self.header = header

    def set_data(self, data=''):
        self.data = data
        self.response_content = self.header + self.data  # 待响应发送数据

    def start_server(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind((self.host, self.port))
            sock.listen(MAX_CONN)  # 监听
            print 'http server %s:%d is  listening... ' % (self.host,self.port)

            self.conn, addr = sock.accept()  # 接收客户端连接
            print 'http server accepted, addr:%s' % str(addr)

            self.request = self.conn.recv(RECV_LEN) # 接收数据
            print 'request is:', self.request
            return True
        except:
            print 'http server exception!'
            return False

    def check_request(self, request_path='/', request_params=''):
        # 解析请求并检查
        try:
            request_list = self.request.split(' ')
            print 'request_list:', request_list
            method = request_list[0]
            src = request_list[1]
            print 'method is:', method
            print 'src is:', src

            src_list = src.split('/')
            parse_request_params = src_list[-1]
            parse_request_path = src.replace(parse_request_params, '')

            # 解析请求参数
            parse_request_params_str = urllib.unquote(parse_request_params).replace('\n', '')
            parse_request_params_dic = json.loads(parse_request_params_str)
            request_params_dic = json.loads(request_params)

            if (method == 'GET') and (parse_request_params_dic == request_params_dic) and (parse_request_path == request_path):
                return True
            else:
                return False
        except:
            print 'exception!'
            return False

    def send_response(self):
        self.conn.sendall(self.response_content)
        #self.conn.close()

if __name__ == '__main__':
    testhttpd = http_server('127.0.0.1',8002)
    testhttpd.set_header()
    testhttpd.set_data('testingqqqqqqqq!!!')
    testhttpd.start_server()
    print testhttpd.check_request()
    testhttpd.send_response()


