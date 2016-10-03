#coding=utf8
import sys

#stdin, stdout, stderr在Python中无非都是文件属性的对象，他们在Python启动时自动与Shell环境中的标准输入，输出，出错关联
print sys.stdin

print sys.stdout

print sys.stderr

'''
包含与标准I/O流对应的流对象, 如果需要更好地控制输出,而print不能满足要求, 它们就是所需要的。 也可以替换它们, 这时候就可以重定向输出和输入到其它
设备(device), 或者以非标准的方式处理它们
'''


#stdout
sys.stdout.write('Hello World!\n')

#stderr
sys.stderr.write('Dive in\n')


#stdin
print 'Hi, %s!' % raw_input('Please enter your name:')

print 'Please enter your name too:',
name = sys.stdin.readline()[:-2]
print 'Hi, %s!  haha!' % name


