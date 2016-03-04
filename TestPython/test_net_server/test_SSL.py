#coding=utf8
'''
python实现SSL的方法：
1）内置SSL支持
2）OpenSSL库
'''

#内置SSL
import socket
HOST = '127.0.0.1'
PORT = 50007
#cmd = raw_input("Please input cmd:")       #与人交互，输入命令
cmd = "GET / HTTP/1.0\r\n\r\n"

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

ssl = socket.ssl(s)
sendall(ssl, cmd)
s.shutdown()

while 1:
    try:
        buf = ssl.read(1024)
    except socket.sslerror, e:
        if e[0] in [socket.SSL_ERROR_ZERO_RETURN, socket.SSL_ERROR_EOF]:
            break
        elif e[0]  in [socket.SSL_ERROR_WANT_READ, socket.SSL_ERROR_WANT_WRITE]:
            continue
        raise
    if len(buf) == 0:
        break
    sys.stdout.write(buf)

s.close()   #关闭连接


#OpenSSL库
HOST = '127.0.0.1'
PORT = 50007
cmd = "GET / HTTP/1.0\r\n\r\n"

#create ssl context object
cex = SSL.Context(SSL.SSLv23_METHOD)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ssl = SSL.Connection(cex, s)


ssl.connect((HOST,PORT))
ssl.sendall(cmd)

while 1:
    try:
        buf = ssl.read(4096)
    except SSL.ZeroReturnError:
        break
    sys.stdout.write(buf)

ssl.close()
