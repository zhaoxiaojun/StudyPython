#coding=utf8

def echo(o):
    print o

class ObjectCreator(object):
    pass
'''
将在内存中创建一个对象，名字就是ObjectCreator。这个对象（类）自身拥有创建对象（类实例）的能力，而这就是为什么它是一个类的原因。但是，它的本质仍然是一个对象。
'''
print ObjectCreator   #可以打印一个类，因为它其实也是一个对象

echo(ObjectCreator)   #可以将类做为参数传给函数

ObjectCreator.new_attribute = 'foo'  #可以为类增加属性
print hasattr(ObjectCreator, 'new_attribute')

ObjectCreatorMirror = ObjectCreator   #可以将类赋值给一个变量
print ObjectCreatorMirror()

my_object = ObjectCreator()
print my_object



#动态创建类
def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo     #返回的是类，不是类的实例
    else:
        class Bar(object):
            pass
        return Bar

MyClass = choose_class('foo')
print MyClass
print MyClass()

