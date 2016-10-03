#coding=utf8
"""
检查字符串中的结束标记
"""
import itertools
import os


def anyTrue(func, seq):
    return True in itertools.imap(func, seq)

def endsWith(s, *endings):
    return anyTrue(s.endswith, endings)


for filename in os.listdir('.'):
    if endsWith(filename, '.jpg', '.jpeg', '.git', '.py'):
        print filename


print '###########################################################'

for filename in os.listdir('.'):
    if anyTrue(filename.endswith, ('.jpg', '.jpeg', '.git', '.py')):
        print filename

print '###########################################################'

for filename in os.listdir('.'):
    if True in map(filename.endswith, ('.jpg', '.jpeg', '.git', '.py')):
        print filename
