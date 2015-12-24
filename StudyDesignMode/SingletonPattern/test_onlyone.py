#coding=utf8
'''
单例模式是一个创建型的设计模式，功能是确保运行时对某个类只存在单个实例对象，并且提供一个全局的访问点来访问这个实例对象。
'''

class OnlyOne(object):
    class __OnlyOne(object):
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg
    def __getattr__(self, name):   #获取属性；内建getattr()；仅在属性没有找到时调用
        return getattr(self.instance, name)

x = OnlyOne('sausage')
print type(x)
print x
print id(x.instance)
print str(x.instance)
print x.instance
print `x.instance`
print x.val

y = OnlyOne('eggs')
print type(y)
print y
print id(y.instance)
print `y.instance`
print y.val

print `x.instance`
print x.val


'''
通过代理的方式进行访问，使用__getattr__()方法将所有调用指向单例
虽然看起来好像创建了多个对象(OnlyOne)，但 __OnlyOne对象只有一个。虽然OnlyOne实例有多个，但他们都是唯一的 __OnlyOne对象的代理
'''
z = OnlyOne('spam')
print z
print id(z.instance)
print `z.instance`
print z.val

print `y.instance`
print y.val
print `x.instance`
print x.val

print '\n---------------------------\n'
