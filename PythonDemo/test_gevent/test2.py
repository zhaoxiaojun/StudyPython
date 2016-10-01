#coding=utf8
import socket
import select

"""
select是一种阻塞调用，专门用于从一些文件描述符中，选出那些有新事件到达的描述符，其中事件包括可读、可写和出错

原型： select.select(rlist, wlist, xlist[, timeout])
参数：
rlist: 等待直到准备好读
wlist: 等待直到准备好写
xlist: 等待一种意外的情况

功能：确定一个或多个套接口的状态。对每一个套接口，调用者可查询它的可读性、可写性及错误状态信息。select是一个直接调用unix中select()的简单接口
"""
sockets = {}
for i in range(100):
    s = socket.socket()
    sockets[s.fileno()] = s
    s.setblocking(0)  #设置socket为非阻塞的，当socket为非阻塞式的时候，如果所做的动作将导致阻塞，将会引起error异常
    try:
        s.connect(('www.baidu.com', 80))
    except Exception as e:
        while sockets:  #监视给出的socket，任何一个有动静了就立即返回有动静的描述符
            fds = select.select([], list(sockets.keys()), [])[1]
            for fd in fds:
                s = sockets.pop(fd)
                print("%d connected to %s:%d" % ((fd,) + s.getpeername()))


