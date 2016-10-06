#coding=utf8
import pexpect
import sys

'''
SSH登录
'''

child = pexpect.spawn('ssh root@121.40.226.14')
fout = file('test2_log.txt', 'w')
child.logfile = sys.stdout
#child.logfile = fout


child.expect("password:")
child.sendline("wjdgusdn0820ABC")

# print 'before: ' + child.before
# print 'after: ' + child.after

child.expect('#')
child.sendline('ls /home')
child.expect('#')

# print 'before: ' + child.before
# print 'after: ' + child.after
