#coding=utf8
import random
from guppy import hpy
'''
通过这个包可以知道在代码执行的每个阶段中，每种类型（str、tuple、dict等）分别创建了多少对象
'''

def random_sort3(n):
    hp = hpy()
    print "Heap at the beginning of the functionn", hp.heap()
    l = [random.random() for i in range(n)]
    l.sort()
    print "Heap at the end of the functionn", hp.heap()
    return l

if __name__ == "__main__":
    random_sort3(2000000)
