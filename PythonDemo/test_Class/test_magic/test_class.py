#coding=utf8

'''
python中一切都是对象，每个对象都包含一个__class__属性以标记其所属类型。
每个对象（记得一切都是对象啊）都包含一个__dict__属性以存储所有属性和方法。
每个类型都包含一个__bases__属性以标记其父类
'''

class counter(object):
    count = 0

    def __init__(self):
        self.__class__.count += 1

print counter.count

c = counter()
print c.count

print counter.count

d = counter()
print d.count

print c.count
print counter.count

print '\n------------------------\n'
e = counter()
print counter.__bases__
print e.__dict__

print '\n------------------------\n'
#对于任何一个__class__的__class__属性（原类：type）
age = 35
print age.__class__
print age.__class__.__class__

name = 'bob'
print name.__class__
print name.__class__.__class__

def foo(): pass
print foo.__class__
print foo.__class__.__class__

class Bar(object): pass
print Bar.__class__            #type
print Bar.__class__.__class__  #type实际上是它自己的元类

b = Bar()
print b.__class__
print b.__class__.__class__
print '\n------------------------\n'
