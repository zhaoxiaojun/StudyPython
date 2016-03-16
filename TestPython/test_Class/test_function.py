#coding=utf8

#在python中，def定义的函数与类中的方法有很大的不同，两者是不同的类型

def foo():
    print "foo"

class A(object):
    def bar(self):  #类中的方法是绑定方法，会具体绑定到某一类的实例。当方法被调用时，实例对象会作为第一个参数(self)，被传入到方法中一个类中的可调用属性一直是未绑定，当类被实例化为一个对象时才绑定到某一具体实例上
        print "bar"
a = A()

print foo
print a.bar
print '\n--------------------------\n'

def fooFighters(self):
    print "fooFighters"

A.fooFighters = fooFighters  #给类增加方法

a2 = A()
print a2.fooFighters   #通过实例调用类增加的方法

a2.fooFighters()

print '\n--------------------------\n'


def barFighters(self):
    print "barFighters"

a.barFighters = barFighters  #把方法直接添加到一个实例对象时，函数并没有自动与与实例对象进行绑定。其仍然是一个函数类型，而不是一个绑定方法
print a.barFighters
#a.barFighters() #error

print '\n--------------------------\n'

#可以使用types模块中的MethodType函数显示绑定函数到某一个实例对象上
import types
a.barFightersAbcd = types.MethodType(barFighters, a)
print a.barFightersAbcd
a.barFightersAbcd()


"""
python中创建一个实例的方法有三种方式：
1、直接在类中定义方法
2、将一个函数赋值给类的属性
3、通过types.MethodType动态地(给实例)创建方法
"""
