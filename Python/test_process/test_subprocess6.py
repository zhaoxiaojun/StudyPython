#coding=utf8
import subprocess

'''
可以在Popen()建立子进程的时候改变标准输入、标准输出和标准错误，并可以利用subprocess.PIPE将多个子进程的输入和输出连接在一起，构成管道(pipe)
subprocess.PIPE实际上为文本流提供一个缓存区。child1的stdout将文本输出到缓存区，随后child2的stdin从该PIPE中将文本读取走。child2的输出文本
也被存放在PIPE中，直到communicate()方法从PIPE中读取出PIPE中的文本。
'''


child1 = subprocess.Popen(["cat","/etc/hosts"], stdout=subprocess.PIPE)

child2 = subprocess.Popen(["grep","dev1.tataufo.com"],stdin=child1.stdout, stdout=subprocess.PIPE)

out = child2.communicate()

print out


