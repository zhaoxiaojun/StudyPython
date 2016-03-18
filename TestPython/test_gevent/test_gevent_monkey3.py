#coding=utf8
import time

def echo(i):
    time.sleep(0.001)
    return i


from gevent.pool import Pool        #greenlet具有确定性。在相同配置相同输入的情况下，它们总是 会产生相同的输出

p = Pool(10)
run1 = [a for a in p.imap_unordered(echo, xrange(10))]
print run1
run2 = [a for a in p.imap_unordered(echo, xrange(10))]
print run2
run3 = [a for a in p.imap_unordered(echo, xrange(10))]
run4 = [a for a in p.imap_unordered(echo, xrange(10))]

print(run1 == run2 == run3 == run4)
