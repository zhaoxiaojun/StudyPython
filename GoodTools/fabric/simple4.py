#coding=utf8
#部署LNMP业务服务环境
from fabric.api import *
from fabric.colors import *

env.user='root'
env.roledefs = {   #定义业务角色分组
    'webservers': ['192.168.1.21',],
    'dbservers': ['192.168.1.22',]
}

env.passwords = {
    'root@192.168.1.21:22': 'xxxx',
    'root@192.168.1.22:22': 'xxxx'
}

@roles('webservers')
def webtask():
    print yellow('Install nginx php...')
    with.settings(warn_only=True):
        run('yum -y install nginx')
        run('yum -y install php-fpm')
        run('chkconfig --levels 235 php-fpm on')
        run('chkconfig --levels 235 nginx on')

@roles('dbservers')
def dbtask():
    print yellow('Install mysql...')
    with.settings(warn_only=True):
        run('yum -y install mysql mysql-server')
        run('chkconfig --levels 235 mysqld on')

@roles('webservers', 'dbservers')
def publictask():    #部署公共类环境
    print yellow('Install public...')
    with.settings(warn_only=True):
        run('rpm -Uvh http://xxxx.rpm')
        run('yum -y install ntp')

def deploy():
    execute(publictask)
    execute(webtask)
    execute(dbtask)
















