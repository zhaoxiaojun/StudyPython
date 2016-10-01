#coding=utf8

class Borg3:
    _state  = {}
    def __init__(self):
        self.__dict__ = self._state
        self.state = 'Init'

    def __str__(self):
        return self.state

class YourBorg(Borg3):
    pass


rm1 = Borg3()
print rm1
print rm1.state
print rm1._state
print rm1.__dict__

rm2 = Borg3()
print rm2
print rm2.state
print rm2._state
print rm2.__dict__

print id(rm1)
print id(rm2)  # different !

print '\n---------------\n'

rm1.state = 'Idle'
rm2.state = 'Running'
print rm1.state
print rm2.state

print('rm1: {0}'.format(rm1))
print('rm2: {0}'.format(rm2))

print '\n---------------\n'
rm2.state = 'Zombie'

print('rm1: {0}'.format(rm1))
print('rm2: {0}'.format(rm2))

print '\n-----------------------------------------------\n'

rm3 = YourBorg()

print('rm1: {0}'.format(rm1))
print('rm2: {0}'.format(rm2))
print('rm3: {0}'.format(rm3))
