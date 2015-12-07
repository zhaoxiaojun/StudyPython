#coding=utf8
import sys #  模块，sys指向这个模块对象
import inspect
def foo(): pass # 函数，foo指向这个函数对象

class Cat(object): # 类，Cat指向这个类对象
    def __init__(self, name='kitty'):
        self.name = name
    def sayHi(self): #  实例方法，sayHi指向这个方法对象，使用类或实例.sayHi访问
        print self.name, 'says Hi!' # 访问名为name的字段，使用实例.name访问

Ocat = Cat() # Ocat是Cat类的实例对象
Otest = Ocat.sayHi

#检查对象是否为模块、类、函数、方法、内建函数或方法
print inspect.ismodule(Otest)
print inspect.isclass(Otest)
print inspect.isfunction(Otest)
print inspect.ismodule(Otest)
print inspect.isbuiltin(Otest)
print '...\n'

print inspect.isroutine(Otest)  #检查对象是否为函数、方法、内建函数或方法等等可调用类型

print inspect.getmembers(Otest)  #这个方法是dir()的扩展版，它会将dir()找到的名字对应的属性一并返回，形如[(name, value), ...]。另外，predicate是一个方法的引用，如果指定，则应当接受value作为参数并返回一个布尔值，如果为False，相应的属性将不会返回

#print inspect.getfile(Otest)            #获取object的定义所在的模块的文件名|源代码文件名（如果没有则返回None）
#print inspect.getsourcefile(Otest)

#print inspect.getsource(Otest)  #获取object的定义的源代码，以字符串|字符串列表返回 只能用于module/class/function/method/code/frame/traceack对象
#print inspect.getsourcelines(Otest)
print '...\n'

print inspect.getargspec(Otest)     #仅用于方法，获取方法声明的参数，返回元组，分别是(普通参数名的列表, *参数名, **参数名, 默认值元组)。如果没有值，将是空列表和3个None

def add(x, y=1, *z):
    print inspect.getargvalues(inspect.currentframe()) #仅用于栈帧，获取栈帧中保存的该次函数调用的参数值
    return x + y + sum(z)
add(2)

#inspect.getcallargs(func[, *args][, **kwds])  #返回使用args和kwds调用该方法时各参数对应的值的字典。这个方法仅在2.7版本中才有。
print inspect.currentframe()  #返回当前的栈帧对象。

print '...其他的操作frame和traceback的函数'
