#coding=utf8
import subprocess

'''
子进程的标准输入、标准输出和标准错误如下属性分别表示:
child.stdin
child.stdout
child.stderr

'''

child1 = subprocess.Popen(["ls","-l"], stdout=subprocess.PIPE)

print child1.stdout.read()
