#coding=utf8
import stackless
"""
微线程间通信
"""

chn = stackless.channel()

def send():
    chn.send("test1")
    print "I Send: test"

def recv():
    print "I Recv:", chn.receive()

stackless.tasklet(send)
stackless.tasklet(recv)
stackless.run()


