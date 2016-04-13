#coding=utf8
import multiprocessing
import time
'''
守护进程就是不阻挡主程序退出，自己干自己的
'''

def worker(interval):
    print("work start:{0}".format(time.ctime()));
    time.sleep(interval)
    print("work end:{0}".format(time.ctime()));

if __name__ == "__main__":
    p = multiprocessing.Process(target=worker, args = (3,))
    p.daemon = True   #因子进程设置了daemon属性，主进程结束，子进程就随着结束
    p.start()
    #p.join()
    print "end!"
