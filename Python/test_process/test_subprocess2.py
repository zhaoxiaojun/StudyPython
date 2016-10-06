#coding=utf8
import subprocess

retcode = subprocess.call("ls -l",shell=True)

print retcode

'''
shell默认为False
在Linux下，shell=False时, Popen调用os.execvp()执行args指定的程序；shell=True时，如果args是字符串，Popen直接调用系统的Shell来执行args指定
的程序，如果args是一个序列，则args的第一项是定义程序命令字符串，其它项是调用系统Shell时的附加参数

在Windows下，不论shell的值如何，Popen调用CreateProcess()执行args指定的外部程序。如果args是一个序列，则先用list2cmdline()转化为字符串，但需
要注意的是，并不是MS Windows下所有的程序都可以用list2cmdline来转化为命令行字符串
'''
