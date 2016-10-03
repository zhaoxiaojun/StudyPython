#coding=utf8
import threading, time
import sys

def sleepandprint():
    time.sleep(1)
    print "heelo from both of us"

def threadcode():
    time.sleep(3)
    sys.stdout.write("hello from the new thread. My name is %s\n" % threading.currentThread().getName())

print "Before starting a new thread, My name is ", threading.currentThread().getName()
t = threading.Thread(target=threadcode, name='Childthreadasdfasfsadsadf')

t.setDaemon(1)
t.start()   #启动子线程后，程序开始分支了

sys.stdout.write("hello from the main thread. My name is %s\n" % threading.currentThread().getName())
sleepandprint()
#t.join()  #阻塞直到t终止
print 11111111111111111111111111111111111111
