#coding=utf8
"""
方法2：共享属性
所谓单例就是所有引用(实例、对象)拥有相同的状态(属性)和行为(方法)，同一个类的所有实例天然拥有相同的行为(方法),只需要保证同一个类的所有实例具有相同的状态(属性)
即可，所有实例共享属性的最简单最直接的方法就是__dict__属性指向(引用)同一个字典(dict)
"""

class Borg(object):
    _state = {}
    def __new__(cls, *a, **k):
        obj = super(Borg, cls).__new__(cls, *a, **k)
        obj.__dict__ = cls._state
        return obj

class MyClass(Borg):
    a = 1


one = MyClass()
two = MyClass()

two.a = 3
print one.a

#one和two是不同的对象
print id(one)
print id(two)
print one == two
print one is two

#但是one和two具有相同的属性字典
print one.__dict__
print two.__dict__

print id(one.__dict__)

print id(two.__dict__)


