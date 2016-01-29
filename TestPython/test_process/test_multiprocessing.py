#coding=utf8
'''
python中的多线程其实并不是真正的多线程，如果想要充分地使用多核CPU的资源，在python中大部分情况需要使用多进程
multiprocessing支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件
'''
import multiprocessing      #multiprocessing模块跨平台
import os, time, random


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__=='__main__':
    print "CPU count: ",multiprocessing.cpu_count()
    print('Parent process %s.' % os.getpid())
    p = multiprocessing.Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    print "p.pid:", p.pid
    print "p.name:", p.name
    print "p.is_alive:", p.is_alive()
    print "p.exitcode:", p.exitcode  #进程在运行时为None、如果为–N，表示被信号N结束
    print "p.authkey:", p.authkey
    p.join()
    print('Child process end.')

