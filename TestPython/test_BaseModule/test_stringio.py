#coding=utf8
from io import StringIO
'''
很多时候，数据读写不一定是文件，也可以在内存中读写。StringIO顾名思义就是在内存中读写str。
要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可
'''
f = StringIO()
f.write(u'hello')
f.write(u'\n')
f.write(u'world!')


print ff.getvalue().split()[0]  #getvalue()方法用于获得写入后的str



# ff = StringIO(u'Hello!\nHi!\nGoodbye!')
# while True:
#     s = ff.readline()
#     if s == '':
#         break
#     print s.strip()

# '''
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes
# '''
# from io import BytesIO

# f = BytesIO()
# f.write(u'中文'.encode('utf-8'))   #写入的不是str，而是经过UTF-8编码的bytes
# print(f.getvalue())

# data = u'人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
# f = BytesIO(data)
# print(f.read())

# f.write(b'world!')
# print(f.getvalue())

