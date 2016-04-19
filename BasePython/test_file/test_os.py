#coding=utf8
import os, shutil

print os.name #操作系统名字 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统

#print os.uname  #uname()函数在Windows上不提供

#print os.environ  #操作系统中定义的环境变量

#print os.getenv('PATH')  #获取某个环境变量的值

#os.putenv(key, value)  #设置环境变量

print os.path.abspath('.')  #目录的绝对路径


#在某个目录下创建一个新目录:
newdir = os.path.join('D:\\CODE\\StudyPython\\BasePython\\test_file', 'testdir') #首先把新目录的完整路径表示出来  把两个路径合成一个正确处理不同操作系统的路径分隔符
print newdir
os.mkdir(newdir)  #然后创建一个目录

#os.makedirs('D:\\CODE\\StudyPython\\BasePython\\test_file\\test1\\test2')  #创建多级目录

#删掉一个目录:
os.rmdir(newdir)


#拆分路径 拆分为两部分 后一部分总是最后级别的目录或文件名
print os.path.split('/Users/michael/testdir/file.txt')

print os.path.dirname('/path/to/file.txt')  #拆分出目录

print os.path.basename('/path/to/file.txt') #拆分出文件名

#拆分出文件扩展名（后一部分）
print os.path.splitext('/path/to/file.txt')

#对文件(或目录)重命名
#os.rename('test1.txt', 'chon1.py')

#删掉文件
#os.remove('test1.py')

#当前目录下的所有文件（包括目录）
print os.listdir('.')

#过滤出目录
print [x for x in os.listdir('.') if os.path.isdir(x)]

#过滤出.log文件
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.txt']


print '============================================================'

print os.getcwd()  #当前工作目录

#os.removedirs(r'D:\\CODE\\StudyPython\\BasePython\\test_file') #删除多个目录

print os.path.exists('D:\\CODE\\StudyPython\\BasePython\\test_file')  #检验给出的路径是否真地存在

#运行shell命令
print os.system('ipconfig')

print os.linesep  #当前平台使用的行终止符 Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'

print os.stat('test2.txt')  #获取文件属性

#os.chmod('out.log') #修改文件权限与时间戳

#os.exit()  #终止当前进程

print os.path.getsize('test2.txt')  #获取文件大小

print '============================================================'

#复制文件
shutil.copyfile("oldfile.txt","newfile.txt")       #oldfile和newfile都只能是文件

#shutil.copy("oldfile","newfile")            #oldfile只能是文件夹，newfile可以是文件，也可以是目标目录

#复制文件夹：
#shutil.copytree("olddir","newdir")        #olddir和newdir都只能是目录，且newdir必须不存在

#移动文件（或目录）
#shutil.move("oldpos","newpos")

#删除目录
#os.rmdir("dir")    #只能删除空目录
#shutil.rmtree("dir")    #空目录、有内容的目录都可以删

#转换目录
#os.chdir("path")   #换路径
