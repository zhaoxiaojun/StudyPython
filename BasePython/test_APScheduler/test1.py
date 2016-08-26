#coding=utf8

from apscheduler.schedulers.blocking import BlockingScheduler

def my_job():
    print 'hello world'

"""
使用BlockingScheduler，并使用默认内存存储和默认执行器。(默认选项分别是MemoryJobStore和ThreadPoolExecutor，其中线程池的最大线程数为10)
"""
sched = BlockingScheduler()
sched.add_job(my_job, 'interval', seconds=5) #每5s执行一次
sched.start()

