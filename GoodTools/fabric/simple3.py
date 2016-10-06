#coding=utf8
from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

#文件打包、上传与校验

env.user = 'root'
env.hosts = ['121.40.226.14',]
env.password = 'wjdgusdn0820ABC'

@task
@runs_once
def tar_task():   #文件打包任务
    with lcd('/data/logs'):
        local('tar -czf access.tar.gz access.log')

@task
def put_task():   #文件上传任务
    run('mkdir -p /data/logs')
    with cd('/data/logs'):
        with.settings(warn_only=True): #出现异常时继续执行，非终止
            result = put('/data/logs/access.tar.gz', '/data/logs/access.tar.gz')
            if result.failed and not confirm('put file failed, continue[Y/N]?'):  #有用户选择是否继续capture=True才能捕获返回值
                abort('Abort file put task!')

@task
def check_task():  #文件校验任务
    with.settings(warn_only=True):
        lmd5 = local('md5sum /data/logs/access.tar.gz', capture=True).split(' ')[0]  #本地local命令需要配置
        rmd5 = run('md5sum /data/logs/access.tar.gz', capture=True).split(' ')[0]
    if lmd5==rmd5:
        print('OK')
    else:
        print('ERROR')

@task
def go():
    tar_task()
    put_task()
    check_task()


'''
fab -f simple3.py tar_task
fab -f simple3.py go
'''

