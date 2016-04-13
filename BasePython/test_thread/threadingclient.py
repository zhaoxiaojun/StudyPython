#coding=utf8
# 客户端多线程
import socket, sys, time
from threading import *

host =  sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]

cv = Condition()
spinners = '|/-\\'
spinpos = 0
equeue = []

def fwrite(buf):
    sys.stdout.write(buf)
    sys.stdout.flush()

def spin():
    global spinpos
    fwrite(spinners[spinpos] + "\b")
    spinpos += 1
    if spinpos >= len(spinners):
        spinpos = 0

def uithread():
    while 1:
        cv.acquire()
        while not len(equeue):
            cv.wait(0.15)
            spin()

        msg = equeue.pop(0)
        cv.release()
        if msg == 'QUIT':
            fwrite("\n")
            sys.exit(0)
        fwrite("\n %s\r" % msg)

def msg(message):
    cv.acquire()
    equeue.append(message)
    cv.notify()
    cv.release()

t = Thread(target=uithread)
t.setDaemon(1)
t.start()

try:
    msg('create socket object')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    print 'strange error creating socket: %s' % e
    sys.exit(1)

try:
    port = int(textport)
except ValueError:
    try:
        port = socket.getservbyname(textport, 'tcp')
    except socket.error, e:
        print 'couldnot find your port: %s' % e
        sys.exit(1)

msg('connecting to %s:%d' % (host, port))
time.sleep(5)
try:
    s.connect((host,port))
except socket.gaierror, e:
    print "address-related error connecting to server:%s" % e
    sys.exit(1)
except socket.error, e:
    print "Connection error: %s" % e
    sys.exit(1)


msg('sending query')
time.sleep(5)
try:
    s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
except socket.error, e:
    print "error send data: %s" % e
    sys.exit(1)


msg('shutting  down socket')
time.sleep(5)
try:
    s.shutdown(1)
except socket.error, e:
    print "Error sending data (delected by shutdown): %s" % e
    sys.exit(1)

msg('Receiving data')
count = 0
while 1:
    try:
        buf =  s.recv(2048)
    except socket.error, e:
        print "Error recving data: %s" % e
        sys.exit(1)
    if not len(buf):
        break
    count += len(buf)

msg("Receiving %d bytes" % count)
msg("QUIT")
t.join()

















