#coding=utf8
"""
readlines方式读取，一次将所有行读到内存中
"""
import os
import timeit
filename = os.getcwd() + "\\test.txt"

def readtest():
    with open(filename, "r+") as fp:
        lines = fp.readlines()  #读出的每行文本木末尾都带有“\n”符号
        #lines = fp.read().splitlines()
        #lines = fp.read().split('\n')
        print 'type of lines: ', type(lines)
        for line in lines:
            pass
            #print line


print timeit.timeit('readtest()', 'from __main__ import readtest', number=100)

# try:
#     fp = open(filename, "r+")
#     lines = fp.readlines()
#     for line in lines:
#         print line
# except IOError as err:
#     print('error: ' + str(err))
# finally:
#     fp.close()
