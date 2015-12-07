#coding=utf8
# 服务器多线程

import socket, traceback, os, sys
from threading import *

host = ''
port = 23454

def handlechild(clientsock):
    print "New child", currentThread().getName()
    print "got connection from", clientsock.getpeername()
    while 1:
        data = clientsock.recv(4096)
        if not len(data):
            break
        clientsock.sendall(data)
    clientsock.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)
print 'listening ... '

while 1:
    try:
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    t = Thread(target = handlechild, args = [clientsock])
    t.setDaemon(1)
    t.start()

