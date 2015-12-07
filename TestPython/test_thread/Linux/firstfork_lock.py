#######!/usr/bin/python
#coding=utf8
import os, time
import socket, traceback, sys, fcntl

def getlastaccess(fd, ip):
    fcntl.flock(fd,fcntl.LOCK_SH)       #加共享锁
    try:
        fd.seek(0)
        for line in fd.readlines():
            fileip, accesstime = line.strip().split("|")
            if fileip == ip:
                return accesstime
        return None
    finally:
        fcntl.flock(fd, fcntl.LOCK_UN) #解锁

def writelastaccess(fd, ip):
    fcntl.flock(fd, fcntl.LOCK_EX) #加独占锁
    records = []
    try:
        fd.seek(0)
        for line in fd.readlines():
            fileip, accesstime = line.strip().split("|")
            if fileip != ip:
                records.append((fileip, accesstime))
        fd.seek(0)

        records_l = records + [(ip, time.asctime())]
        for fileip, accesstime in records_l:
            print '%d---write data...' % os.getpid()
            fd.write("%s|%s_%d\n" % (fileip, accesstime,os.getpid()))
        fd.truncate()
    finally:
        fcntl.flock(fd, fcntl.LOCK_UN)  #解锁

def reap():
    while 1:
        try:
            result = os.waitpid(-1, os.WNOHANG) #等待所有已经终止的子进程，如果没有已经终止的进程存在就立刻返回，如果有子进程在等待，返回一个进程PID的tuple和退出信息
            if not result[0]: break
        except:
            break
        print "%d---Reap child process %d" % (os.getpid(),result[0])

HOST = '192.168.18.77'
PORT = 51423

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(5)   #最大连接数
print '%d---start listening...' % os.getpid()
fd = open("lastaccess.txt", "w+")

while 1:
    try:
        clientsock, clientaddr = sock.accept()
        print '%d---start accepting...' % os.getpid()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    reap()

    try:
        print '%d---fork stating...' % os.getpid()
        pid = os.fork()
        print '%d---fork ended' % os.getpid()
    except:
        print "BAD THING HAPPENED: fork failed"
        clientsock.close()
        continue

    if pid:                   #父进程
        print '%d---I am father' % os.getpid()
        print 'My pid is %s' % os.getpid()
        print 'My son pid is %s' % str(pid)
        print 'My father pid is %s' % os.getppid()
        clientsock.close()
        continue

    else:                      #子进程
        print '%d---I am son' % os.getpid()
        print 'My pid is %s' % os.getpid()
        print 'My father pid is %s' % os.getppid()
        sock.close()
        try:
            print "Got connect from %s, serving with pid %d " % (clientsock.getpeername(), os.getpid())
            ip = clientsock.getpeername()[0]
            clientsock.sendall("welcome %s\n" % ip)
            last = getlastaccess(fd,ip)
            if last:
                print '%d---send data1...' % os.getpid()
                clientsock.sendall("%d---I last saw you at %s\n" % (os.getpid(), last))
            else:
                print '%d---send data2...' % os.getpid()
                clientsock.sendall("%d---I've never seen you before\n" % os.getpid())
            print '%d---call writelastaccess...' % os.getpid()
            writelastaccess(fd, ip)
            print '%d---send data3...' % os.getpid()
            clientsock.sendall("%d---I have noted your connection at %s.\n" % (os.getpid(),getlastaccess(fd,ip)))
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            traceback.print_exc()

        try:
            clientsock.close()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()

        sys.exit(0)
