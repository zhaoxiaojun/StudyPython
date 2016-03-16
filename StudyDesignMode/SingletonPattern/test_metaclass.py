#coding=utf8
"""
方法3：本质上是方法1的升级（或者说高级）版
使用__metaclass__（元类）的高级python用法
"""

class Singleton2(type):
    def __init__(cls, name, bases, dict):
        super(Singleton2, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton2, cls).__call__(*args, **kw)
        return cls._instance

class MyClass3(object):
    __metaclass__ = Singleton2

one = MyClass3()
two = MyClass3()

two.a = 3
print one.a

print id(one)  # The same !!
print id(two)

print one == two
print one is two

