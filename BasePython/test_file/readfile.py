#coding=utf8
"""
readline方式读取，每次读一行
"""
import os
import timeit
filename = os.getcwd() + "\\test.txt"

def readtest():
    with open(filename, "r+") as fp:
        line = fp.readline()
        while line:
            #print line
            pass
            line = fp.readline()
#readtest()

print timeit.timeit('readtest()', 'from __main__ import readtest', number=100)

# 相当于：

# try:
#     fp = open(filename, "r+")
#     line = fp.readline()
#     while line:
#         print line
#         line = fp.readline()
# except IOError as err:
#     print('error: ' + str(err))
# finally:
#     fp.close()
