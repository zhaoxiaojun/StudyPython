#coding=utf8
import multiprocessing      #multiprocessing模块跨平台
from multiprocessing import Process
from multiprocessing import Pool
import os, time, random


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    '''
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
    '''
    print "CPU count: ",multiprocessing.cpu_count()
    print('Parent process %s.' % os.getpid())
    p = Pool()   #Pool的默认大小是CPU的核数
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()         #对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    print('All subprocesses done.')
