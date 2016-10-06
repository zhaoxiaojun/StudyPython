#coding=utf8
import pexpect


'''
run: 使用pexpect进行封装的调用外部命令的函数，类似于os.system和os.popen方法，可以同时获得命令的输出结果和退出状态
定义：pexpect.run(command, timeout=-1, withexitstatus=False, events=None, extra_args=None, logfile=None, cwd=None, env=None)
events：字典，定义了expect及sendline方法的对应关系
'''

res = pexpect.run('ssh root@121.40.226.14', timeout=3, events={'password:':'wjdgusdn0820ABC'})

print res

'''
等价于：
child = pexpect.spawn('ssh root@121.40.226.14')
child.expect("password:")
child.sendline("wjdgusdn0820ABC")
'''
