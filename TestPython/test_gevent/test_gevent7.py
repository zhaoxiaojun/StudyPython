#coding=utf8
import gevent
from gevent import Timeout

seconds = 10

timeout = Timeout(seconds)
timeout.start()

def wait():
    gevent.sleep(10)

try:
    gevent.spawn(wait).join()
except Timeout:
    print('Could not complete')

print '\n----------------\n'


# #超时类也可以用在上下文管理器(context manager)中, 也就是with语句内

# time_to_wait = 5 # seconds
# class TooLong(Exception):
#     pass

# with Timeout(time_to_wait, TooLong):
#     gevent.sleep(10)

