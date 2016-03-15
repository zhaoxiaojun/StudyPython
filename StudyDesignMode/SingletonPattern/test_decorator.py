#coding=utf8
#通过使用装饰器的方式：

def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class MyClass4(object):
    a = 1
    def __init__(self, x=0):
        self.x = x

one = MyClass4()
two = MyClass4()

two.a = 3

print one.a

print id(one)
print id(two)


print one == two
print one is two


one.x = 1
print one.x
print two.x
