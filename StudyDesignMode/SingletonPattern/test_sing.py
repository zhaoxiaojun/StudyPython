#coding=utf8
#通过_new__的方式：

# ---------- Singletone ----------
# Real Singleton instance
class Singleton(object):
    def __new__(type):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance

    def ppp(self,s):
        return s

# ---------- Alex's Martelli examples ----------
class Singleton2(object):
    def __new__(cls, *a, **k):
        if not hasattr(cls, '_inst'):
            #cls._inst = super(Singleton2, cls).__new__(cls, *a, **k)
            cls._inst = object.__new__(cls, *a, **k)
        return cls._inst

    def ppp(self,s):
        return s



a = Singleton2()
a.toto = 12

b = Singleton2()


print b.toto

print id(a), id(b)  # The same !!

print a.ppp('aaa')

print b.ppp('bbb')




