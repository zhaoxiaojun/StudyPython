#!/usr/bin/python
#coding=utf8

import os,time

#创建子进程之前声明的变量
source = 10
print 'first getpid: ', os.getpid()

try:
    forkn = os.fork()
    if forkn == 0: #子进程
        print "this is child process."
        print 'forkn is ',forkn
        #在子进程中source自减1
        source = source - 1

    else: #父进程
        time.sleep(30)
        print "this is parent process."
        print 'forkn is',forkn

    print 'source: ', source
    print 'getpid: ', os.getpid()
    print 'getppid: ', os.getppid()
except OSError, e:
    print 'oserror!'
    pass
