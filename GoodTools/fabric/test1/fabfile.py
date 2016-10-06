#coding=utf8
from fabric.api import local

def hello():
    print("Hello world!")



def hello2(name="world"):   #参数值只能作为Python字符串来使用
    print("Hello %s!" % name)

def prepare_deploy():
    local("python test.py")  #local执行本地Shell命令并与之交互
    local("git status")



'''
执行：
fab hello
fab hello2:name=Jeff
fab prepare_deploy

Fabric如果执行过程出现错误，将会终止执行，不会继续
'''
