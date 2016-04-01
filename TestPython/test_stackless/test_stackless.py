#coding=utf8
import stackless
"""
stackless python是python的一个增强版本，修改了python的代码，提供对微线程的支持，微线程即轻量级线程，与线程相比，切换时间更少，资源占用更少
"""


def show():
    print 'testing'

stackless.tasklet(show)
stackless.tasklet(show)
stackless.run()


st = stackless.tasklet(show)()
print st.alive
st.run()
#st.kill()
print st.alive

