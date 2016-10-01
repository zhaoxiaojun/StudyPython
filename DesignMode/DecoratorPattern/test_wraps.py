#coding=utf8
from functools import wraps


def makebold(fn):
    return getwrapped(fn, "b")


def makeitalic(fn):
    return getwrapped(fn, "i")


def getwrapped(fn, tag):
    @wraps(fn)
    def wrapped():
        return "<%s>%s</%s>" % (tag, fn(), tag)
    return wrapped


@makebold
@makeitalic
def hello():
    """a decorated hello world"""
    return "hello world"

if __name__ == '__main__':
    print('result:{}   name:{}   doc:{}'.format(hello(), hello.__name__, hello.__doc__))
