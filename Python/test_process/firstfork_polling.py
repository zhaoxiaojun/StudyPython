#coding=utf8
import os, time

def reap():
    while 1:
        try:
            result = os.waitpid(-1, os.WNOHANG)
        except:
            break
        print 'reap child process %d' % result[0]

print 'Before the fork, my pid is: ', os.getpid()

pp = os.fork()
print 'pp is ',pp
if pp:
    print 'Hello from the parent, getpid is ', os.getpid()
    print 'sleep 60s...'
    time.sleep(60)
    print 'sleep done!'
    reap()
    print 'sleep 60s...'
    time.sleep(60)
    print 'sleep done!'

else:
    time.sleep(30)
    print 'child sleep done!'
