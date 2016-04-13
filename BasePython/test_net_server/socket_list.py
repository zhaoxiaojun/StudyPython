#coding=UTF8
"""
 打印所有python安装机器上的socker选项
"""
import socket

solist = [x for x in dir(socket) if x.startswith('SO_')]
solist.sort()

for x in solist:
    print x

print "----------"

sollist = [x for x in dir(socket) if x.startswith('SOL_')]
sollist.sort()

for x in sollist:
    print x
