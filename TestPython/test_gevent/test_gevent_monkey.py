#coding=utf8
import socket
from gevent import monkey
import select

"""
gevent能够修改标准库里面大部分的阻塞式系统调用，包括socket、ssl、threading和 select等模块，而变为协作式运行
"""

print(socket.socket)
print("After monkey patch")
monkey.patch_socket()
print(socket.socket)


print(select.select)
monkey.patch_select()
print("After monkey patch")
print(select.select)
