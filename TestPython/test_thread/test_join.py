#coding=utf8
import threading
import time

def context(tJoin):
    print 'in threadContext.'
    tJoin.start()

    # 将阻塞tContext直到threadJoin终止。
    tJoin.join()

    # tJoin终止后继续执行。
    print 'out threadContext.'

def join():
    print 'in threadJoin.'
    time.sleep(1)
    print 'out threadJoin.'

tJoin = threading.Thread(target=join)
tContext = threading.Thread(target=context, args=(tJoin,))

tContext.start()
