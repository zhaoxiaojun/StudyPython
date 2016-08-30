#coding=utf8
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cookie = self.get_secure_cookie("count")  #取得浏览器的cookies
        count = int(cookie) + 1 if cookie else 1

        countString = "1 time" if count == 1 else "%d times" % count

        self.set_secure_cookie("count", str(count))   #设置浏览器的cookies

        self.write(
            '<html><head><title>Cookie Counter</title></head>'
            '<body><h1>You’ve viewed this page %s times.</h1>' % countString +
            '</body></html>'
        )

"""
Tornado将cookie值编码为Base-64字符串，并添加了一个时间戳和一个cookie内容的HMAC签名。如果cookie的时间戳太旧（或来自未来），或签名和期望值不匹配
，get_secure_cookie()函数会认为cookie已经被篡改，并返回None，就好像cookie从没设置过一样。
"""

if __name__ == "__main__":
    tornado.options.parse_command_line()

    settings = {
        "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E="  #需要指定一个唯一的随机字符串   import base64, uuid; base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
        #"xsrf_cookies": True  #使用Tornado的XSRF保护 当这个应用标识被设置时，Tornado将拒绝请求参数中不包含正确的_xsrf值的POST、PUT和DELETE请求
    }

    application = tortnado.web.Application([
        (r'/', MainHandler)
    ], **settings)

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


"""
然而，Tornado的安全cookies仍然容易被窃听。攻击者可能会通过脚本或浏览器插件截获cookies，或者干脆窃听未加密的网络数据。记住cookie值是签名的而不是
加密的。恶意程序能够读取已存储的cookies，并且可以传输他们的数据到任意服务器，或者通过发送没有修改的数据给应用伪造请求。因此，避免在浏览器cookie
中存储敏感的用户数据是非常重要的。
"""
