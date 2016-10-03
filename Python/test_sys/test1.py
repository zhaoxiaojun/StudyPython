#coding=utf8
import sys

print 'sys.argv: ', sys.argv  #命令行参数列表
print len(sys.argv)  #命令行参数个数
print sys.argv[0]  #脚本名

if len(sys.argv) == 1:
   print "NO canshu"
else:
    n = 1
    for i in sys.argv[1:]:
        strcanshu = str(i)
        print  'di',n,'ge canshu shi',strcanshu
        n = n + 1


print sys.platform  #运行平台
'''
平台                            值
Linux (2.x and 3.x)           'linux2'
Windows                       'win32'
Windows/Cygwin                'cygwin'
Mac OS X                      'darwin'
OS/2                          'os2'
OS/2 EMX                      'os2emx'
RiscOS                        'riscos'
AtheOS                        'atheos'
'''

print sys.modules
print sys.modules.keys()
'''
Python中所有加载到内存的模块都放在sys.modules中
当import一个模块时首先会在这个列表中查找是否已经加载了此模块，如果加载了则只是将模块的名字加入到正在调用import的模块的Local名字空间中。如果
没有加载则从sys.path目录中按照模块名称查找模块文件，模块文件可以是py、pyc、pyd，找到后将模块载入内存，并加入到sys.modules中，并将名称导入到
当前的Local名字空间
'''








