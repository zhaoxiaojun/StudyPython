#coding=utf8
from timeit import timeit as timeit

'''
timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000)
'''

#简短示例：

print(timeit("math.sqrt(2.0)", "import math"))

print(timeit("sqrt(2.0)", "from math import sqrt"))

def test():
    print 'tests'


print(timeit("test()", "from __main__ import test", number=1000))
