#coding=utf8
from fabric.api import *

#查看本地与远程主机信息

env.user = 'root'
env.hosts = ['121.40.226.14',]
env.password = 'wjdgusdn0820ABC'


@runs_once    #只运行1次，不受多台主机影响
def local_task():    #本地任务函数
    local('uname -a')


def remote_task():
    with cd('/home'):   #with上下文管理器，让后面执行的语句继承当前状态
        run('ls -l')



'''
fab -f simple1.py local_task
fab -f simple1.py remote_task
'''
