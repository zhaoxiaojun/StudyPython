#coding=utf8

class testc1(object):
    name = None

    @classmethod
    def hehe(cls):
        cls.name = cls.__name__


print testc1.name
testc1.hehe()
print testc1.name
