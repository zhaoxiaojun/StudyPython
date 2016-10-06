#coding=utf8
import subprocess

'''
一个进程可以fork一个子进程，通过标准库中的subprocess包来fork一个子进程，并运行一个外部的程序
subprocess包中定义有数个创建子进程的函数，这些函数分别以不同的方式创建子进程，所以我们可以根据需要来从中选取一个使用。另外subprocess还提供了
一些管理标准流(standard stream)和管道(pipe)的工具，从而在进程间使用文本通信
'''


r = subprocess.call(['nslookup', 'www.python.org'])
'''
父进程等待子进程完成 返回退出信息(returncode，相当于Linux exit code)
'''
print type(r)
print('Exit code:', r)




c1 = subprocess.check_call(['ping','-c', '2', 'www.baidu.org'])
'''
父进程等待子进程完成  返回0
检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError，该对象包含有returncode属性，可用try…except…来检查
'''
print('Exit code:', c1)





c2 = subprocess.check_output(['ping','-c', '2', 'www.baidu.org'])
'''
父进程等待子进程完成  返回子进程向标准输出的输出结果
检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError，该对象包含有returncode属性和output属性，output属性为标准输出的输出结果，可用try…except…来检查
'''
print('output:', c2)






