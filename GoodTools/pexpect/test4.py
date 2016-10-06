#coding=utf8
from pexpect import pxssh
import getpass

'''
pxssh是pexpect的派生类，针对在ssh会话操作上再做一层封装，提供比基类更加直接的方法
定义： class pexpect.pxssh.pxssh(timeout=30, maxread=2000, searchwindowsize=None, logfile=None, cwd=None, env=None)
方法：
login() 建立ssh连接
logout() 断开连接
prompt() 等待系统提示符，用于等待命令结束
'''

try:
    s = pxssh.pxssh()
    hostname = raw_input('hostname: ')
    username = raw_input('username: ')
    password = getpass.getpass('please input password: ')
    s.login(hostname, username, password)
    s.sendline('uptime')  #运行uptime命令
    s.prompt()
    print s.before

    s.sendline('ls -l')
    s.prompt()
    print s.before

    s.sendline('df')
    s.prompt()
    print s.before

    s.logout()   #断开ssh连接
except pxssh.ExceptionPxssh, e:
    print 'pxssh failed on login'
    print str(e)
