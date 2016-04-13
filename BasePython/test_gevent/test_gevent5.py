#coding=utf8
import gevent

"""
一个greenlet的状态通常是一个依赖于时间的参数。在greenlet中有一些标志， 让你可以监视它的线程内部状态：
started -- Boolean, 指示此Greenlet是否已经启动
ready() -- Boolean, 指示此Greenlet是否已经停止
successful() -- Boolean, 指示此Greenlet是否已经停止而且没抛异常
value -- 任意值, 此Greenlet代码返回的值
exception -- 异常, 此Greenlet内抛出的未捕获异常
"""



def win():
    return 'You win!'

def fail():
    raise Exception('You fail at failing.')

winner = gevent.spawn(win)
loser = gevent.spawn(fail)

print(winner.started) # True
print(loser.started)  # True


try:
    gevent.joinall([winner, loser])
except Exception as e:
    print('This will never be reached')

print(winner.value) # 'You win!'
print(loser.value)  # None

print(winner.ready()) # True
print(loser.ready())  # True

print(winner.successful()) # True
print(loser.successful())  # False


print(loser.exception)
