#coding=utf8
'''
Pool可以提供指定数量的进程，供用户调用，当有新的请求提交到pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到
规定最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来它
'''
import multiprocessing
import os, time


# 子进程要执行的代码
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print "CPU count: ",multiprocessing.cpu_count()
    print('Parent process %s.' % os.getpid())
    p = multiprocessing.Pool(processes = 3)   #不指定时Pool的默认大小是CPU的核数
    for i in xrange(4):
        p.apply_async(long_time_task, args=(i,))  #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
                                                  #apply_async(func[, args[, kwds[, callback]]]) 它是非阻塞
                                                  #apply(func[, args[, kwds]])是阻塞的
    print('Waiting for all subprocesses done...')
    p.close()        # 关闭pool，使其不在接受新的任务
    p.join()         #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束。 join方法要在close或terminate之后使用
    print('All subprocesses done.')

"""
执行说明：
创建一个进程池pool，并设定进程的数量为3，xrange(4)会相继产生四个对象[0, 1, 2, 4]，四个对象被提交到pool中，因pool指定进程数为3，所以0、1、2会直接送到进程中
执行，当其中一个执行完事后才空出一个进程处理对象3。 因为为非阻塞，主函数会自己执行自个的，不搭理进程的执行，所以运行完for循环后直接输出。主程序在pool.join()
处等待各个进程的结束
"""
