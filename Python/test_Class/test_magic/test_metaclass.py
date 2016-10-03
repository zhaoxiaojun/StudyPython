#coding=utf8

'''
元类： 就是用来创建类的“东西。type就是Python在背后用来创建所有类的元类
type能动态的创建类，type可以接受一个类的描述作为参数，然后返回一个类

type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
'''

MyShinyClass = type('MyShinyClass', (), {})   #返回一个类对象，等价于： class MyShinyClass(object): pass
print MyShinyClass
print MyShinyClass()     #创建一个该类的实例

Foo = type('Foo', (), {'bar':True})   #等价于：class Foo(object): bar = True
FooChild = type('FooChild', (Foo,),{})  #等价于：class FooChild(Foo): pass

print '\n------------------------\n'



#type就是Python的内建元类，当然也可以创建自己的元类
class Foo(Bar):
    pass

"""
当写下如上代码时，Python做了如下的操作:
Foo中有__metaclass__这个属性吗？如果是，Python会在内存中通过__metaclass__创建一个名字为Foo的类对象。如果Python没有找到__metaclass__，它会继续在Bar（父类）中
寻找__metaclass__属性，并尝试做和前面同样的操作。如果Python在任何父类中都找不到__metaclass__，它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作。如果
还是找不到__metaclass__,Python就会用内置的type来创建这个类对象。
"""
#自定义元类
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))    #选择所有不以'__'开头的属性
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)    #将它们转为大写形式
    return type(future_class_name, future_class_parents, uppercase_attr)   #通过'type'来做类对象的创建

__metaclass__ = upper_attr  #这会作用到这个模块中的所有类。__metaclass__实际上可以被任意调用，它并不需要是一定是一个正式的类中。

class Foo(object):
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'

print hasattr(Foo, 'bar')  #False

print hasattr(Foo, 'BAR')  #True

f = Foo()
print f.BAR    #'bip'
print '\n------------------------\n'


'''
__new__是在__init__之前被调用的特殊方法，__new__是用来创建对象并返回之的方法，而__init__只是用来将传入的参数初始化给对象。很少用到__new__，除非你希望能够控制对象
的创建。这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__，如果你希望的话，你也可以在__init__中做些事情。 还有一些高级的用法会涉及到改写
__call__特殊方法，但是我们这里不用
'''
class UpperAttrMetaClass(type):   #'type'实际上是一个类就像'str'和'int'一样，所以可以从type继承
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):   #类方法的第一个参数总是表示当前的实例，就像在普通的类方法中的self参数一样
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return type(future_class_name, future_class_parents, uppercase_attr)


class UpperAttrMetaclass2(type):
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return type.__new__(upperattr_metaclass, future_class_name, future_class_parents, uppercase_attr) #复用type.__new__方法

class UpperAttrMetaclass3(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__')
        uppercase_attr  = dict((name.upper(), value) for name, value in attrs)
        return type.__new__(cls, name, bases, uppercase_attr)

class UpperAttrMetaclass4(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return super(UpperAttrMetaclass4, cls).__new__(cls, name, bases, uppercase_attr)


#用元类来搞些“黑暗魔法”是特别有用的：拦截类的创建、修改类、 返回修改之后的类


'''
“元类就是深度的魔法，99%的用户应该根本不必为此操心。如果你想搞清楚究竟是否需要用到元类，那么你就不需要它。那些实际用到元类的人都非常清楚地知道他们需要做什么，
而且根本不需要解释为什么要用元类。”  —— Python界的领袖 Tim Peters
'''

#元类的主要用途是创建API。一个典型的例子是Django ORM
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
guy  = Person(name='bob', age='35')
print guy.age
'''
这并不会返回一个IntegerField对象，而是会返回一个int，甚至可以直接从数据库中取出数据。这是有可能的，因为models.Model定义了__metaclass__， 并且使用了一些魔法
能够将你刚刚定义的简单的Person类转变成对数据库的一个复杂hook。Django框架将这些看起来很复杂的东西通过暴露出一个简单的使用元类的API将其化简，通过这个API重新创
建代码，在背后完成真正的工作。
'''


'''
结论：
类其实是能够创建出类实例的对象。事实上类本身也是实例，它们是元类的实例。
Python中的一切都是对象，它们要么是类的实例，要么是元类的实例，除了type。type实际上是它自己的元类，在纯Python环境中这可不是你能够做到的，这是通过在实现层面耍
一些小手段做到的。其次，元类是很复杂的。对于非常简单的类，你可能不希望通过使用元类来对类做修改。你可以通过其他两种技术来修改类：Monkey patching、class decorators
当你需要动态修改类时，99%的时间里你最好使用上面这两种技术。当然了，其实在99%的时间里你根本就不需要动态修改类。
'''
