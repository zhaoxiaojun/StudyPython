#coding=utf8
import os,os.path

def VisitDir(arg,pathname,filenames):
    print 'arg: ',arg
    print 'pathname: ', pathname
    print 'filenames: ', filenames
    arg[0].append('qqq')
    for filename in filenames:
        print os.path.join(pathname,filename)
    print '\n\n'



if __name__=="__main__":
    path="/opt"
    sss = list()
    arg = (sss,1,2,3)
    os.path.walk(path,VisitDir,arg)
    print arg[0]


"""
函数声明：walk(top,func,arg)
1>参数top表示需要遍历的目录树的路径
2>参数func表示回调函数，对遍历路径进行处理.所谓回调函数，是作为某个函数的参数使用，当某个时间触发时，程序将调用定义好的回调函数处理某个任务.回调函数必须提供3个参数：第1个参数为walk()的参数arg，第2个参数表示路径，第3个参数表示文件(含目录)列表
3>参数arg是传递给回调参数func的元组.回调函数的一个参数必须是arg，为回调函数提供处理参数.参数arg可以为空
"""


