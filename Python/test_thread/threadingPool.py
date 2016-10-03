#coding=utf8
import socket
import traceback
import os, time, sys
from threading import *

def listener():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)

    while  1:
        try:
            clientsock,clientaddr = s.accept()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()
            continue

        handleconnection(clientsock)

def handleconnection(clientsock):
    lockpool.acquire()
    print 'recived new client connection'
    try:
        if len(waitinglist) == 0 and (activeCount() - 1) >= MAXTHREADS:
            clientsock.close()
            return
        if len(waitinglist) == 0:
            startthread()
        queue.append(clientsock)
        sem.release()
    finally:
        lockpool.release()

def startthread():
    print 'starting new client processor thread'
    t = Thread(target = threadworker)
    t.setDaemon(1)
    t.start()

def threadworker():
    global waitinglist, lockpool, busylist
    time.sleep(1)
    name = currentThread().getName()
    try:
        lockpool.acquire()
        try:
            waitinglist[name] = 1
        finally:
            lockpool.release()

        processclients()
    finally:
        if name in waitinglist:
            del waitinglist[name]
        if name in busylist:
            del busylist[name]
        # start a replacement thread
        startthread()

def processclients():
    global sem, queue, waitinglist, busylist, lockpool
    name = currentThread().getName()
    while 1:
        sem.acquire()
        lockpool.acquire()
        try:
            clientsock = queue.pop(0)
            del waitinglist[name]
            busylist[name] = 1
        finally:
            lockpool.release()

        try:
            print "[%s] got connection from %s" % (name, clientsock.getpeername())
            clientsock.sendall('you are being serviced by %s \n' % name)
            while 1:
                data = clientsock.recv(4096)
                if data.startswith('DIE'):
                    sys.exit()
                if not len(data):
                    break
                clientsock.sendall(data)
        except (KeyboardInterrupt,SystemExit):
            raise
        except:
            traceback.print_exc()

        #close the connection
        try:
            clientsock.close()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()

        lockpool.acquire()
        try:
            del busylist[name]
            waitinglist[name] = 1
        finally:
            lockpool.release()

if __name__ == '__main__':
    host = ''
    port = 12345
    MAXTHREADS = 3
    lockpool = Lock()
    busylist = {}
    waitinglist = {}
    queue = []
    sem = Semaphore(0)

    listener()
