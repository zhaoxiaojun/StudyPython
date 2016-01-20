#coding=utf8

class BaseClass(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print 'baseclass is inited'

    def speak(self, name):
        print 'base class is speak: %s' % name


class SubClass(BaseClass):
    def talk(self, sth):
        print sth
'''
基类的初始化方法会被子类继承，子类重写初始化方法需要显示调用
'''

SO = SubClass('a','b')
SO.talk('123')
print SO.name
print SO.age
