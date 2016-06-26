#coding=utf8
"""
更好的方式
"""
import os
import timeit

filename = os.getcwd() + "\\test.txt"


def readtest():
    with open(filename, "r+") as fp:
        for line in fp: #这样读出的每行文本末尾也带有“\n”符号
            line = line.rstrip('\n')  #去除
            pass
            #print line


print timeit.timeit('readtest()', 'from __main__ import readtest', number=100)
