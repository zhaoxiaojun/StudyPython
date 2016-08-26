#encoding: utf-8
from functools import update_wrapper

def wrap(func):
    def call_it(*args, **kwargs):
        """wrap func: call_it"""
        print 'before call'
        return func(*args, **kwargs)
    return call_it

@wrap
def hello():
    """say hello"""
    print 'hello world'



def wrap2(func):
    def call_it(*args, **kwargs):
        """wrap func: call_it2"""
        print 'before call'
        return func(*args, **kwargs)
    return update_wrapper(call_it, func)

@wrap2
def hello2():
    """test hello"""
    print 'hello world2'

if __name__ == '__main__':
    hello()
    print hello.__name__
    print hello.__doc__

    print
    hello2()
    print hello2.__name__
    print hello2.__doc__


"""
这个函数主要用在装饰器函数中，装饰器返回函数反射得到的是包装函数的函数定义而不是原始函数定义
"""
