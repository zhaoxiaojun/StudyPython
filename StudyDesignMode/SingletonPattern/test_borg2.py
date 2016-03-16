#coding=utf8

class Borg2:
    _state = {}
    def __init__(self):
        self.__dict__ = self._state

a = Borg2()
a.toto = 12
print a.__dict__


b = Borg2()
print b.__dict__
print b.toto

print id(a)
print id(b)    # different ! but states are sames

print a.__dict__
print b.__dict__
