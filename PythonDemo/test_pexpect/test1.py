#coding=utf8
import pexpect

child = pexpect.spawn('sudo locust -h')
i = child.expect([pexpect.EOF, pexpect.TIMEOUT, 'Password:'])
#i为匹配到的在列表中的序号，0开始
if i==0:
    print('0000000')
elif i==1:
    print('1111111')
    # child.sendline('vt100')
    # child.expect('[#\$] ')
elif i==2:
    print('2222222')
