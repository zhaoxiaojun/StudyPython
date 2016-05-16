#coding=utf8
import os
import time
import subprocess

"""
孤儿进程：一个父进程退出，而它的一个或多个子进程还在运行，那么那些子进程将成为孤儿进程。孤儿进程将被init进程(进程号为1)所收养，并由init进程对它们完成状态收集工作。
僵尸进程：一个进程使用fork创建子进程，如果子进程退出，而父进程并没有调用wait或waitpid获取子进程的状态信息，那么子进程的进程描述符仍然保存在系统中。这种进程称之为僵死进程。
"""

if __name__ == '__main__':
    p = subprocess.Popen('ipconfig',shell=True,bufsize=-1,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    file =  p.stdout.readlines()
    p.wait()
    """
    wait()会暂时停止目前进程的执行，直到有信号来到或子进程结束。如果在调用wait()时子进程已经结束，则wait()会立
    即返回子进程结束状态值。子进程的结束状态值会由参数status返回，子进程的进程识别码也会一块返回。
    """


    for i in range(0, len(file)):
        print file[i]


    while True:
        time.sleep(1)

