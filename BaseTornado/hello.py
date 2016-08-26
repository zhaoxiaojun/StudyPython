#coding=utf8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

#命令行默认参数及类型
define("port", default=8000, help="run on the given port", type=int)

#处理器
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')

if __name__ == "__main__":
    #套路：
    #解析命令行
    tornado.options.parse_command_line()

    #通过处理器handler获得app
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])

    #app转为server
    http_server = tornado.httpserver.HTTPServer(app)

    #设置server监听端口
    http_server.listen(options.port)

    #启动server
    tornado.ioloop.IOLoop.instance().start()
