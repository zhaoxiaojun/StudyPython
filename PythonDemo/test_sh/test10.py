#coding=utf8
import sh
import threading
from time import sleep
#with sudo



def worker(username):
    with sh.sudo('-u', username, _with=True):
        sleep(3)
        print username, sh.id()

t1 = threading.Thread(target=worker, args=('tataufo',))
t2 = threading.Thread(target=worker, args=('root',))

t1.start()
sleep(1)
t2.start()
