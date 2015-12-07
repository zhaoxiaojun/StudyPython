#coding=UTF8
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import json


def jiexi_json():
    f = open('response_data.json', 'r')
    s = f.read()
    #u = s.decode('gb2312')
    #str = s.encode('utf-8')
    k = json.loads(s)
    print k
    return k

data = jiexi_json()


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            global data
            buf = data

            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(buf)
        except:
            print 'yget error!'


def xxxx():
    try:
        httpd_address = ('localhost', 8011)
        myhttpd = HTTPServer(httpd_address, MyHTTPRequestHandler)
        myhttpd.serve_forever()

    except  KeyboardInterrupt:
        myhttpd.socket.close()

if __name__ == '__main__':
    #jiexi_json()
    xxxx()
