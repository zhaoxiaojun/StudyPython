#coding=utf8
import __builtin__

def open(path):
    f = __builtin__.open(path, 'r')
    return UpperCaser(f)

class UpperCaser:
    __metaclass__ = type

    def __init__(self, f):
        self._f = f

    def read(self):
        return self._f.read().upper()

print open('./a.txt').read()  #将会全部转为大写输出


