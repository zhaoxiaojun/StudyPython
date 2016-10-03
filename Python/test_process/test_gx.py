#coding=utf8
'''
应该尽量避免共享状态
共享内存方式:
'''
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in xrange(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))
    print 'type num: ', type(num)
    print 'type arr: ', type(arr)
    print 'num: ', num
    print 'arr: ', arr
    print 'num.value: ', num.value
    print 'arr[:]: ', arr[:]

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print num.value
    print arr[:]
