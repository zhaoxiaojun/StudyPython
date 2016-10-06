#coding=utf8
from fabric.api import *
from fabric.contrib.console import confirm

'''
git代码提交项目部署示例
'''

env.hosts = ['my_server']  #指定Fabric一次性控制多台远程服务器的方法：env.hosts是一个列表，fab对它迭代，对每个连接运行指定的任务

def test():
    with settings(warn_only=True):
        result = local('./manage.py test my_app', capture=True)  #manage.py创建数据库等工作
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

def commit():
    local("git add -p && git commit")

def push():
    local("git push")

def prepare_deploy():
    test()
    commit()
    push()

def deploy():
    code_dir = '/srv/django/myproject'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone user@vcshost:/path/to/repo/.git %s" % code_dir)
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")


