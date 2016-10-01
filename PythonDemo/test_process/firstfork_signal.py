#coding=utf8
import os, time, signal

def childhandler(signum, stackframe):
    while 1:
        try:
            result = os.waitpid(-1, os.WNOHANG)
        except:
            break
        signal.signal(signal.SIGCHLD, childhandler) #重新激活信号处理函数，因为有些unix在信号处理程序被调用的时候会使它无效，通过外在激活，你可以确保下一个子进程终止时它被调用

signal.signal(signal.SIGCHLD, childhandler)

print 'Before the fork, my pid is: ', os.getpid()

pp = os.fork()
print 'pp is ',pp
if pp:
    print 'Hello from the parent, getpid is ', os.getpid()
    print 'sleep 30s...'
    time.sleep(60)  #如果任意一个信号处理程序被调用，睡眠会被立刻终止，而不会继续等待剩余的时间
    print 'sleep done!'
else:
    time.sleep(30)
    print 'child sleep done!'
