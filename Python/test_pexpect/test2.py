#coding=utf8
import pexpect
import time
import uuid

#配置（待做成命令行）
config = "tataufo_index"


#日志文件名
now = time.strftime("%Y-%m-%d %H-%M-%S")
uuid = uuid.uuid1()
logfile = "tataufo_shiningrun_" + str(now) + str(uuid) + ".log"
logfile = "".join(logfile.split())


#启动
cmd = 'sudo nohup locust -f %s.py --logfile=logs/%s &' % (config, logfile)
print(cmd)
print("start...")

child = pexpect.spawn(cmd)

#有时需要输入root密码
#i = child.expect(['Password:', pexpect.EOF, pexpect.TIMEOUT, '\"nohup.out\"'])
i = child.expect(['Password:', pexpect.EOF], timeout=None)
if i==0:
    print("input Password")
    child.sendline('mC7uE5wJ')
elif i==1:
    print("EOF")
    pass

try:
    child.expect('\"nohup.out\"',timeout=None)
    child.sendline('\n')
except Exception, e:
    print e
    print("nohup error!")

#pexpect让出控制权
# print('out pexpect')
# child.interact()
