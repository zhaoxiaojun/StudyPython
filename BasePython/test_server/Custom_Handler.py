#coding=UTF8
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class Get_Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            buf = 'Get data'

            self.protocol_version = 'HTTP/1.1'
            self.send_response(200, 'okok')

            self.send_header('welcome', 'contect')
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(buf)

        except:
            print 'YZH get error!'
            #self.send_error(404, 'File Not Found: %s' % self.path)

class Post_Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            buf = 'Post data'

            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)

            self.send_header('welcome', 'contect')
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(buf)
        except:
            print 'YZH post error!'

if __name__ == '__main__':
    httpd_address = ('localhost', 8011)
    myhttpd = HTTPServer(httpd_address, Get_Handler)
    myhttpd.serve_forever()
