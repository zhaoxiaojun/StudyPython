#coding=utf8
"""
同方法3
"""
# Real Singleton instance
class Singleton(object):
    def __new__(type):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance

    def ppp(self,s):
        return s


one = Singleton()
two = Singleton()

two.a = 3
print one.a

print id(one)  # The same !!
print id(two)

print one == two
print one is two
