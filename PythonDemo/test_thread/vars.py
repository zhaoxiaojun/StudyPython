#coding=utf8
#共享变量
import threading, time

a = 50
b = 50
c = 50
d = 50

def printvars():
    print 'a=', a
    print 'b=', b
    print 'c=', c
    print 'd=', d

def threadcode():
    global a,b,c,d
    a += 50
    b = b + 50
    c = 100
    d = 'hello'
    print "[childthread] vaules of variables in child thread:"
    printvars()

print "[Mainthread] vaules of variables in child thread:"
printvars()

t = threading.Thread(target=threadcode, name='childthread')

t.start()
t.join()

print "[Mainthread] vaules of variables in child thread:"
printvars()

#存在潜在的问题：可能发送紊乱
