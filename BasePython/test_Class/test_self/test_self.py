#coding=utf8
#############################################################
#自省（反射）:
#有时候我们会碰到这样的需求，需要执行对象的某个方法，或是需要对对象的某个字段赋值，而方法名或是字段名在编码代码时并不能确定，需要通过参数传递字符串的形式输入。
#举个具体的例子：当我们需要实现一个通用的DBM框架时，可能需要对数据对象的字段赋值，但我们无法预知用到这个框架的数据对象都有些什么字段，换言之，我们在写框架的时候需要
#通过某种机制访问未知的属性。这个机制被称为反射（反过来让对象告诉我们他是什么），或是自省（让对象自己告诉我们他是什么，好吧我承认括号里是我瞎掰的- -#），用于实现在运
#行时获取未知对象的信息。反射是个很吓唬人的名词，听起来高深莫测，在一般的编程语言里反射相对其他概念来说稍显复杂，一般来说都是作为高级主题来讲；但在Python中反射非常简
#单，用起来几乎感觉不到与其他的代码有区别，使用反射获取到的函数和方法可以像平常一样加上括号直接调用，获取到类后可以直接构造实例；不过获取到的字段不能直接赋值，因为拿
#到的其实是另一个指向同一个地方的引用，赋值只能改变当前的这个引用而已。
###############################################################
import sys #  模块，sys指向这个模块对象
import inspect

def foo(canshu='default'):  # 函数，foo指向这个函数对象
    '''testdoc foo'''
    print canshu
    pass
    return 0

class Cat(object): # 类，Cat指向这个类对象
    def __init__(self, name='kitty'):
        self.name = name
    def sayHi(self): #  实例方法，sayHi指向这个方法对象，使用类或实例.sayHi访问
        print self.name, 'says Hi!' # 访问名为name的字段，使用实例.name访问

cat = Cat('kitty')

print cat.name # 访问实例属性
cat.sayHi() # 调用实例方法

print dir(cat) # 获取实例的属性名，以列表形式返回 遇到未知的对象使用dir()是一个很好的主意
if not hasattr(cat, 'name'): # 检查实例是否有这个属性
    setattr(cat, 'name', 'tiger') # same as: a.name = 'tiger'
print getattr(cat, 'name') # same as: print a.name

getattr(cat, 'sayHi')() # same as: cat.sayHi()

#在types模块中定义了全部的Python内置类型，结合内置方法isinstance()就可以确定对象的具体类型
print isinstance(cat, Cat) # 检查object是不是classinfo中列举出的类型，返回布尔值。classinfo可以是一个具体的类型，也可以是多个类型的元组或列表

#查看都有哪些模块是内建的
print sys.builtin_module_names

print "\n--模块module--"
import types as m
print m.__doc__.splitlines()[0] # 文档字符串。如果模块没有文档，这个值是None。
print m.__name__                # 始终是定义时的模块名；即使你使用import .. as 为它取了别名，或是赋值给了另一个变量名
print m.__file__                # 包含了该模块的文件路径。内建的模块没有这个属性
print m.__dict__.items()[0]     # 包含了模块里可用的属性名-属性的字典；也就是可以使用模块名.属性名访问的对象

print "\n--类class--"
print Cat.__doc__           # 文档字符串
print Cat.__name__          # 始终是定义时的类名
print Cat.__module__        # 包含该类的定义的模块名；需要注意，是字符串形式的模块名而不是模块对象
print Cat.__bases__         # 直接父类对象的元组；但不包含继承树更上层的其他类，比如父类的父类 (<type>,)
print Cat.__dict__          # 包含了类里可用的属性名-属性的字典；也就是可以使用类名.属性名访问的对象

print "\n--实例instance--"
print cat.__dict__   #包含了可用的属性名-属性字典
print cat.__class__  #该实例的类对象
print cat.__class__ == Cat # True


print "\n--内建函数和方法built-in functions and methods--"
testO = sys.getsizeof
print testO.__name__  #函数或方法的文档
print testO.__doc__  #函数或方法定义时的名字
print testO.__self__ #仅方法可用，如果是绑定的(bound)，则指向调用该方法的类（如果是类方法）或实例（如果是实例方法），否则为None
print testO.__module__ #函数或方法所在的模块名

print "\n--函数function--"
#非内建的函数。注意，在类中使用def定义的是方法，方法与函数虽然有相似的行为，但它们是不同的概念
print foo.__doc__   #函数的文档；另外也可以用属性名func_doc
print foo.__name__  #函数定义时的函数名；另外也可以用属性名func_name
print foo.__module__  #包含该函数定义的模块名
print foo.__dict__  #函数的可用属性；另外也可以用属性名func_dict
print foo.func_defaults  #这个属性保存了函数的参数默认值元组
print foo.func_code  #这个属性指向一个该函数对应的code对象，code对象中定义了其他的一些特殊属性
print foo.func_globals  #这个属性指向定义函数时的全局命名空间
print foo.func_closure  #这个属性仅当函数是一个闭包时有效，指向一个保存了所引用到的外部函数的变量cell的元组，如果该函数不是一个内部函数，则始终为None。这个属性也是只读的

print "\n--方法method--"
testO = cat.sayHi
print testO.__name__  #与函数相同
print testO.__doc__  #与函数相同
print foo.__module__   #与函数相同
print testO.im_func  #使用这个属性可以拿到方法里实际的函数对象的引用
print testO.im_self  #如果是绑定的(bound)，则指向调用该方法的类（如果是类方法）或实例（如果是实例方法），否则为None
print testO.im_class  #实际调用该方法的类，或实际调用该方法的实例的类。注意不是方法的定义所在的类，如果有继承关系的话
#说明：这里讨论的是一般的实例方法，另外还有两种特殊的方法分别是类方法(classmethod)和静态方法(staticmethod)。类方法还是方法，不过因为需要使用类名调用，所以他始终是绑定的；
#而静态方法可以看成是在类的命名空间里的函数（需要使用类名调用的函数），它只能使用函数的属性，不能使用方法的属性。

print "\n--生成器generator--"
def gen():
    for n in xrange(5):
        yield n
g = gen()

print g             # <generator object gen at 0x...>
print g.__iter__    #仅仅是一个可迭代的标记
print g.gi_code     #生成器对应的code对象
print g.gi_frame    #生成器对应的frame对象
print g.gi_running  #生成器函数是否在执行。生成器函数在yield以后、执行yield的下一行代码前处于frozen状态，此时这个属性的值为0
print g.next()      # 0
print g.next()      # 1
for n in g:
    print n,        # 2 3 4


print "\n--代码块code--"
#代码块可以由类源代码、函数源代码或是一个简单的语句代码编译得到。这里我们只考虑它指代一个函数时的情况；
#可以使用函数的func_code属性获取到它。code的属性全部是只读的。
co = cat.sayHi.func_code
print co.co_argcount        # 普通参数的总数，不包括*参数和**参数。
print co.co_names           # 所有的参数名（包括*参数和**参数）和局部变量名的元组
print co.co_varnames        # 所有的局部变量名的元组
print co.co_flags & 0b100   # 这是一个数值，每一个二进制位都包含了特定信息。较关注的是0b100(0x4)和0b1000(0x8)，如果co_flags & 0b100 != 0，说明使用了*args参数；如果co_flags & 0b1000 != 0，说明使用了**kwargs参数。另外，如果co_flags & 0b100000(0x20) != 0，则说明这是一个生成器函数
print co.co_filename  #源代码所在的文件名


print "\n--栈帧frame--"
#用在当前栈帧时与内建函数globals()相同，但你可以先获取其他帧
def add(x, y=1):
    f = inspect.currentframe()
    print f.f_locals    # 用在当前栈帧时与内建函数locals()相同，但你可以先获取其他帧然后使用这个属性获取那个帧的locals()
    print f.f_back      # 调用栈的前一帧
    print f.f_code      # 栈帧对应的code对象。
    print f.f_globals   #用在当前栈帧时与内建函数globals()相同
    return x+y
add(2)



print "\n--追踪traceback--"
#追踪是在出现异常时用于回溯的对象，与栈帧相反。由于异常时才会构建，而异常未捕获时会一直向外层栈帧抛出，所以需要使用try才能见到这个对象。traceback的属性全部是只读的。
def div(x, y):
    try:
        return x/y
    except:
        tb = sys.exc_info()[2]  # 用sys模块的exc_info()函数获得，这个函数返回一个元组，元素分别是异常类型、异常对象、追踪
        print tb
        print tb.tb_lineno      # 当前追踪的行号
        print tb.tb_next   # 追踪的下一个追踪对象
        print tb.tb_frame  # 当前追踪对应的栈帧
div(1, 0)
