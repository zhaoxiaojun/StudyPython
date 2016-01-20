#coding=utf8
#thread模块
import thread
import time

# 一个用于在线程中执行的函数
def func():
    print '--------'
    for i in range(5):
        print 'func'
        print thread.get_ident()

    # 结束当前线程
    # 这个方法与thread.exit_thread()等价
    thread.exit_thread() # 当func返回时，线程同样会结束
    print '--------'

'''
启动一个线程，线程立即开始运行
thread.start_new_thread(function, args[, kwargs]):
启动一个新线程，并返回线程的标识(就一个int类型的整数，不是对象)。
function是线程的回调函数；args是传递给回调函数的一个tuple；kwargs是可选参数，代表命令行参数的一个字典
等价：start_new方法
'''

print thread.get_ident()
mythread = thread.start_new_thread(func, ()) #方法没有参数时需要传入空tuple
print type(mythread)

"""
lock = thread.allocate()  # 创建一个锁（LockType，不能直接实例化）  这个方法与thread.allocate_lock()等价
print lock.locked()   # 判断锁是锁定状态还是释放状态

# 锁通常用于控制对共享资源的访问
count = 0

'''
lock.acquire([waitflag]):
请求获取锁，成功返回True，否则返回False. waitflag省略或非0值，则无条件等待，直到其它线程释放了锁，本线程能够获取锁，waitflag=0表示无论是否获取成功，
函数马上返回，不等待。
'''
if lock.acquire():
    count += 1
    lock.release() # 释放锁

# thread模块提供的线程都将在主线程结束后同时结束
print 'count:', count
"""
print 'sleep ...'
time.sleep(8)
print 'sleep end'

print mythread

"""
thread.interrupt_main():  在主线程中触发 KeyboardInterrupt 异常。子线程可以使用该方法来中断主线程。
thread.get_ident(): 获得一个代表当前线程的魔法数字(线程的标识)，常用于从一个字典中获得线程相关的数据。这个数字本身没有任何含义，并且当线程结束后会被新线程复用
thread还提供了一个ThreadLocal类用于管理线程相关的数据，名为 thread._local，threading中引用了这个类
thread.exit() : 结束当前线程。调用该函数会触发 SystemExit 异常，如果没有处理该异常，线程将结束。
thread.exit_thread(): 退出线程
"""
