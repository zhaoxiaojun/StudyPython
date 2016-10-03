#coding=utf8
import os, time

print 'Before the fork, my pid is: ', os.getpid()

pp = os.fork()
print 'pp is ',pp
if pp:
    print 'Hello from the parent, getpid is ', os.getpid()
    print 'sleep 30s...'
    time.sleep(30)
