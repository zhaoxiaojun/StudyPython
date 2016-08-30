#coding=utf8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        print self.application.tracker123  #取得myApp中设置的tracker123属性
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!\n')

    def write_error(self, status_code, **kwargs):
        self.write("Gosh darnit, user! You caused a %d error.\n" % status_code)

#App与Handler之间可以通信
class myApp(tornado.web.Application):
     def __init__(self, handlers):
        tornado_settings = dict()
        tornado.web.Application.__init__(self, handlers=handlers, **tornado_settings)
        self.tracker123 = 'defias-track'


if __name__ == "__main__":
    #解析命令行
    tornado.options.parse_command_line()

    #通过处理器handler获得app
    app = myApp(handlers=[(r"/", IndexHandler)])

    #app转为server
    http_server = tornado.httpserver.HTTPServer(app)

    #设置server监听端口
    http_server.listen(options.port)

    #启动server
    tornado.ioloop.IOLoop.instance().start()
