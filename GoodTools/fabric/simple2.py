#coding=utf8
from fabric.api import *

#动态获取远程目录列表


env.user = 'root'
env.hosts = ['121.40.226.14',]
env.password = 'wjdgusdn0820ABC'

@runs_once   #只有第一台触发次函数
def input_raw():
    return prompt('please input directory name: ', default='/home')

def worktask(dirname):
    run('ls -l ' + dirname)

@task   #限定只有go函数对fab可见，其他函数对fab不可见
def go():
    getdirname = input_raw()
    worktask(getdirname)
