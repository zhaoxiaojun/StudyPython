#coding=utf8
import threading
import time

# 通过继承创建线程
class mythread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
    def run(self):
        print threading.currentThread().getName()
        time.sleep(1)
        print 'I am %s' % self.getName()
        print self.id

        class sonsonthread(threading.Thread):
            def __init__(self, id):
                threading.Thread.__init__(self)
                self.id = id
            def run(self):
                time.sleep(1)
                print 'I am %s' % self.getName()
                print self.id
                time.sleep(3)
                print '%s--%s' % (self.getName(),self.id)

        sonsont = sonsonthread(11)
        sonsont.setDaemon(False)
        sonsont.start()

        time.sleep(3)
        print '%s--%s' % (self.getName(),self.id)

print threading.currentThread().getName()
print '---'
t = mythread(1)
t.setDaemon(False)
t.start()
print 'main'
#print t.isAlive()  #打印线程状态 线程是否在运行  正在运行指启动后、终止前
#print t.getName()  #打印线程名
#t.setName('TT')  #设置线程名
#print t.getName()

#print threading.currentThread()  #返回当前的线程实例
#print threading.enumerate()  #返回一个包含正在运行的线程的list
#print threading.activeCount() #返回正在运行的线程数量 与len(threading.enumerate())有相同的结果
print '-----'




"""
# 通过将要执行的方法作为参数传给Thread的构造方法创建线程
def func():
    print 'func() passed to Thread'

t = threading.Thread(target=func)
'''
构造方法：
Thread(group=None, target=None, name=None, args=(), kwargs={})
group: 线程组，目前还没有实现，库引用中提示必须是None；
target: 要执行的方法；
name: 线程名；
args/kwargs: 要传入方法的参数。
'''

t.start()  #启动线程
print t.isAlive()
print t.getName()
t.setName('TT')
print t.getName()
'''
其他方法：
is/setDaemon(bool): 获取/设置是否守护线程。初始值从创建该线程的线程继承。当没有非守护线程仍在运行时，程序将终止。
join([timeout]): 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。
'''
"""
