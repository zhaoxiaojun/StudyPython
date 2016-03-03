#coding=utf8

import mimetypes, sys


#fp = open('email.data', 'r+')
mimetype, mimeencoding = mimetypes.guess_type('email.data')
print mimetype
print mimeencoding



url = 'http://www.baidu.com'
mimetype, mimeencoding = mimetypes.guess_type(url)
print mimetype
print mimeencoding
