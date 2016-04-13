#coding=utf8
'''
装饰器使用最佳实践：
经典的用法是，在函数的外部，扩展一个函数的行为（你不需要改变这个函数），或者，为了调试的目的（我们不修改的原因是这是临时的），你可以使用装饰器扩展一些函数,
而不用在这些函数中书写相同的函数实现一样的功能。
'''

def benchmark(func):
    """
    装饰器打印一个函数的执行时间
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print func.__name__, time.clock()-t
        return res
    return wrapper

def logging(func):
    """
    装饰器记录函数日志
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print func.__name__, args, kwargs
        return res
    return wrapper

def counter(func):
    """
    记录并打印一个函数的执行次数
    """
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print "{0} has been used: {1}x".format(func.__name__, wrapper.count)
        return res
    wrapper.count = 0
    return wrapper

@counter
@benchmark
@logging
def reverse_string(string):
    return str(reversed(string))

print reverse_string("Able was I ere I saw Elba")
print '\n---------------------\n'

print reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!")
print '\n---------------------\n'


