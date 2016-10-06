#coding=utf8
import pexpect
import sys

#远程文件自动打包并下载

ip = ''
user = ''
password = ''
targetfile = '/data/logs/nginx_access.log'  #目标主机nginx日志
child = pexpect.spawn('ssh', [user+'@'+ip])
fout = file('mylog.txt', 'w')
child.logfile = fout
try:
    child.expect('(?i)password')  #(?i)表示不区分大小写
    child.sendline(password)
    child.expect('#')
    child.sendline('tar -zcf /data/nginx_access.tar.gz ' + targetfile)  #打包日志文件
    child.expect('#')
    print child.before
    child.sendline('exit')
    fout.clase()
except EOF:
    print 'EOF'
except TIMEOUT:
    print 'TIMEOUT'

child = pexpect.spawn('scp', [user+'@'+ip+':/data/nginx_access.tar.gz', '/home'])   #远程拷贝
fout = file('mylog.txt', 'a')
child.logfile = fout
try:
    child.expect('(?i)password')
    child.sendline(password)
    child.expect(pexpect.EOF)
except EOF:
    print 'EOF'
except TIMEOUT:
    print 'TIMEOUT'



