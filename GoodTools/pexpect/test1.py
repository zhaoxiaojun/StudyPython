#coding=utf8
import pexpect
import sys

'''
spawn: 启动和控制子应用程序
构造函数：
class pexpect.spawn(command,  #命令
args=[],  #命令参数
tinmeout=30,  #超时时间
maxread=2000,  #pexpect从终端控制台一次读取的最大字节数
searchwindowsize=None,  #匹配缓冲区字符串的位置，默认从开始位置开始匹配
logfile=None,  #日志文件句柄
cwd=None,
env=None,
ignore_sighup=True)

'''
child = pexpect.spawn('/usr/bin/ftp')
child = pexpect.spawn('/usr/bin/ftp', [])

child = pexpect.spawn('/usr/bin/ssh', ['user@example.com'])
child = pexpect.spawn('ls', ['-latr', '/tmp'])


'''
pexpect不会解析shell中的元字符：> >> | *
解决办法：将含有shell元字符的命令作为/bin/bash的参数进行调用
'''
cmd = 'ls -l | grep LOG > logs.txt'
child = pexpect.spawn('/bin/bash',  ['-c', cmd])
#child = pexpect.spawn("/bin/bash -c 'ls -l | grep LOG > logs.txt'")



'''
获取pexpect的输入与输出信息
'''
#写日志文件
child = pexpect.spawn('some_command')
fout = file('mylog.txt', 'w')
child.logfile = fout

#标准输出
child = pexpect.spawn('some_command')
child.logfile = sys.stdout



'''
expect方法定义了一个子程序输出的匹配规则
定义： expect(pattern, timeout=-1, searchwindowsize=-1)
pattern： 表示字符串、pexpect.TINEOUT（超时）、 pexpect.TINEOUT（指向缓冲区尾部、无匹配项）、 正则表达式或之中类型组成的列表（当列表中多个元素
匹配时优先匹配最先出现的元素，即最小索引ID）
timeout：等待匹配结果的超时时间，单位为秒
searchwindowsize：匹配缓冲区字符串的位置，默认从开始位置开始匹配
'''

index = child.expect(['good', 'bad', pexpect.TINEOUT, pexpect.TINEOUT])
if index == 0:
    do_something()
elif index == 1:
    do_something_else()
elif index == 2:
    do_something_other()
elif index == 3:
    do_something_otherother()

#等价于：
try:
    index = child.expect(['good', 'bad'])
    if index == 0:
        do_something()
    elif index == 1:
        do_something_else()
expect EOF:
    do_something_other()
expect TINEOUT:
    do_something_otherother()

'''
expect方法的两个成员：
before: 保存了最近匹配成功之前的内容
after: 保存了最近匹配成功之后的内容
'''


'''
向子程序发送响应命令：
send(string)   ##发送命令不回车
sendline(string)  #发送命令并回车
sendcontrol(char)  #发送控制字符  sendcontrol('c') 发送Ctrl+c
sendeof()   #发送EOF
'''



'''
interact方法：
让出控制权，用户可以继续当前的会话手工控制子程序，默认输出"^]"字符跳出
'''



