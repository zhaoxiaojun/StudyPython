#coding=utf8
import subprocess

p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

output, err = p.communicate(b'set q=mx\npython.org\nexit\n') #communicate()是Popen对象的一个方法，该方法会阻塞父进程，直到子进程完成

print 'output: \n', output
print 'err: \n', err
print('Exit code:', p.returncode)

'''
上面的代码相当于在命令行执行命令nslookup，然后手动输入：
set q=mx
python.org
exit
'''
