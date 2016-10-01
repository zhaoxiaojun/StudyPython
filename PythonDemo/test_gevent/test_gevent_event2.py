#coding=utf8
import gevent
from gevent.event import AsyncResult
"""
事件对象的一个扩展是AsyncResult，它允许你在唤醒调用上附加一个值。 它有时也被称作是future或defered，因为它持有一个指向将来任意时间可设置 为任何值的引用
"""

a = AsyncResult()

def setter():
    """
    After 3 seconds set the result of a.
    """
    gevent.sleep(1)
    a.set('Hello!')
    print '111'

def waiter():
    """
    After 3 seconds the get call will unblock after the setter
    puts a value into the AsyncResult.
    """
    gevent.sleep(3)
    print(a.get())

gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
])
