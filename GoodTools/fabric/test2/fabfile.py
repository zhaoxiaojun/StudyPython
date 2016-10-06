#coding=utf8
from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd
from fabric.contrib.console import confirm

'''
故障处理
'''

def test():
    with settings(warn_only=True):  #settings上下文管理器提供了特定代码块特殊设置的功能（如果出错仅告警）
        result = local('python test.py', capture=True)
    print(result.return_code)  #执行结果返回码
    if result.failed and not confirm("Tests failed. Continue anyway?"):  #confirm函数yes/no提示
        abort("Aborting at user request.")  #abort函数用于手动停止任务的执行
    print('continue...')


def deploy():
    code_dir = '/srv/django/myproject'
    with settings(warn_only=True):
        print(1111)
        if run("test -d %s" % code_dir).failed:  #和调用local一样,run也提供基于Shell命令构建干净的Python逻辑, 不过是在远程而非本地执行
            run("git clone user@vcshost:/path/to/repo/.git %s" % code_dir)
    with cd(code_dir):  #相当于运行cd /srv/django/myproject，和lcd函数类似，只不过后者是在本地执行
        run("git pull")
        run("touch app.wsgi")

'''
执行：
fab test
fab deploy
'''
