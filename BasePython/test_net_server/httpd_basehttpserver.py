#coding=UTF8
'''
BaseHTTPServer 提供基本的Web服务和处理器类，分别是HTTPServer和BaseHTTPRequestHandler
'''
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            #实例变量
            print self.path
            print self.client_address
            print self.command
            print self.request_version
            print self.headers
            print self.rfile #包含一个输入流，定位在可选的输入数据开头
            print self.wfile  #包含写到客户端响应的输出流。当写给这个流时坚持使用正确的HTTP协议

            #实例方法
            """
            handle()
            调用 handle_one_request()一次 (或，如果能够持续连接，多次) 处理进来的 HTTP 请求。你从不需要重载它；替代，实现对应的 do_*() 方法。
            handle_one_request()
            这个方法将解析和分派请求到对应的 do_*() 方法。你从不需要重载它。
            send_error(code[, message])
            发送并记录一个完整的错误回复到客户端。数字的 code 指定 HTTP 错误代码，以 message 作为可选的，更多指定的文本。全套的头被发送，后面紧跟使用 the error_message_format 类变量组成的文本。
            send_response(code[, message])
            发送一个响应头并记录已接收的请求。HTTP 响应行被发送，后面紧跟 Server 和 Date 头。这两个头的值分别地从 version_string() 和 date_time_string() 方法中获得。
            send_header(keyword, value)
            编写一个指定的 HTTP 头到输出流。 keyword 应该指定头关键字，value 指定它的值。
            end_headers()
            发送一个空白行，表示响应中的 HTTP 头结束。
            log_request([code[, size]])
            记录一个已接收的 (成功的) 请求。code 指定关联响应的数字的 HTTP 代码。如果响应的大小可用，那么它应该作为 size 参数被传递。
            log_error(...)
            当一个请求不能被完成时记录一个错误。缺省，它传递信息给 log_message()，因此它取相同的参数 (format 和 附加值)。
            log_message(         format,...)
            记录一个随机信息给 sys.stderr。典型地重载创建自定义的错误日志结构。 format 参数是一个标准的printf风格的格式化字符串，附加参数给 log_message() 用于输出格式。客户端地址和当前的日期时间被作为记录的每个信息的前缀。
            version_string()
            返回服务器软件的版本字符串。这是一个 server_version 和 sys_version 类变量的联合。
            date_time_string([timestamp])
            返回通过 timestamp 给定的日期和时间(必须是由 time.time()返回的格式)，格式化一个信息头。如果 timestamp 被省略，它使用当前的日期和时间。结果像 'Sun, 06 Nov 1994 08:49:37 GMT'。2.5 版本中的新特性： timestamp 参数。
            log_date_time_string()
            返回当前的日期和时间，格式化日志。
            address_string()
            返回客户端地址，格式化日志。一个名称的查找被执行在客户端的IP地址上。
            """

            #test code
            buf = 'It Works'
            #fdata = open(curdir + sep + self.path)

            self.protocol_version = 'HTTP/1.1'
            self.send_response(200, 'okok')

            self.send_header('welcome', 'contect')
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(buf)
            #fdata.close()
        except:
            print 'YZH get error!'
            #self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            #test code
            buf = 'Post data'

            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)

            self.send_header('welcome', 'contect')
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(buf)
        except:
            print 'YZH post error!'


# 主函数
def main():
    try:
        httpd_address = ('localhost', 8011)
        myhttpd = HTTPServer(httpd_address, MyHTTPRequestHandler)
        myhttpd.serve_forever()

    except  KeyboardInterrupt:
        myhttpd.socket.close()

if __name__ == '__main__':
    """
    #类变量
    print MyHTTPRequestHandler.server_version #指定服务器软件版本
    print MyHTTPRequestHandler.sys_version #包含Python系统版本
    print MyHTTPRequestHandler.error_message_format #为构建响应到客户端的错误构建一个格式字符串
    print MyHTTPRequestHandler.protocol_version  #指定在响应中使用的HTTP协议版本
    print MyHTTPRequestHandler.MessageClass  #指定一个类似于rfc822.Message的类解析HTTP头
    print MyHTTPRequestHandler.responses  #包含一个错误代码整数到包含一个短的和一个长的信息的两个元素的元组的映射。例如{code: (shortmessage,longmessage)}。shortmessage 通常被用作错误响应中message关键字，longmessage用作explain关键字 (参阅 error_message_format 类变量)。
    """
    main()
