#coding=utf8
#通过__dict__共享属性的方式：

class Borg:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state

class YourBorg(Borg):
    pass
#------------------------------------
class Borg2(object):
    """Subclassing is no problem."""
    _shared_state = {}
    def __new__(cls, *a, **k):
        obj = super(Borg2, cls).__new__(cls, *a, **k)
        obj.__dict__ = cls._shared_state
        return obj

# ---------- Borg's singletone ----------
class Borg3:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

a = Borg3()
a.toto = 12

b = Borg3()
print b.toto
print id(a), id(b)  # different ! but states are sames





if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()

    rm1.state = 'Idle'
    rm2.state = 'Running'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    rm2.state = 'Zombie'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    print('rm1 id: {0}'.format(id(rm1)))
    print('rm2 id: {0}'.format(id(rm2)))

    rm3 = YourBorg()

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))
    print('rm3: {0}'.format(rm3))

