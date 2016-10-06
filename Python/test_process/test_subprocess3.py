#coding=utf8
import subprocess


'''
class Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False,
cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)

其他的几个方法都是基于Popen()的封装(wrapper)。这些封装的目的在于让我们容易使用子进程。当我们想要更个性化我们的需求的时候，就要转向Popen类，
该类生成的对象用来代表子进程
'''

child = subprocess.Popen(['ping','-c','4','www.baidu.com'])
#child.wait() #等待的情况
#在父进程中对子进程可进行的其它操作：
#child.poll() #检查子进程状态
#child.kill() #终止子进程
#child.send_signal() #向子进程发送信号
#child.terminate() #终止子进程

print 'parent process'  #父程序不会自动等待子进程完成。必须调用对象的wait()方法，父进程才会等待 (也就是阻塞block)


