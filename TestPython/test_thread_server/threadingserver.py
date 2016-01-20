#coding=utf8
import socket
import traceback
import os, time, sys
from threading import *

host = ''
port = 1234

def handlechild(clientsock):
    print 'New child',currentThread().getName()
    print 'Connection from',clientsock.getpeername()
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
