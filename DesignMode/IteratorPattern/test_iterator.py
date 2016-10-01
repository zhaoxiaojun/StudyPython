#coding=utf8
"""
迭代器模式
定义：提供一种方法访问一个容器对象中各个元素，而又不暴露该对象的内部细节
类型：行为类模式
"""

# from a sequence
x = [42, "test", -12.34]
it = iter(x)
try:
    while True:
        x = next(it)  # in Python 2, you would use it.next()
        print x
except StopIteration:
    pass


# a generator
def foo(n):
    for i in range(n):
        yield i

it = foo(5)
try:
    while True:
        x = next(it)  # in Python 2, you would use it.next()
        print x
except StopIteration:
    pass
