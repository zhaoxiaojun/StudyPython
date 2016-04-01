#coding=utf8
import stackless
"""
控制任务执行顺序
"""

def show():
    stackless.schedule()
    print 1
    stackless.schedule()
    print 2


stackless.tasklet(show)
stackless.tasklet(show)
stackless.run()
