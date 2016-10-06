#coding=utf8
'''
Python使用叫做名字空间的东西来记录变量的轨迹。名字空间只是一个字典，它的键就是变量名，值就是那些变量的值。实际上，名字空间可以象Python的字典一
样进行访问
每个函数都有着自已的名字空间，叫做局部名字空间，它记录了函数的变量，包括函数的参数和局部定义的变量
每个模块拥有它自已的名字空间，叫做全局名字空间，它记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量
还有就是内置名字空间，任何模块均可访问它，它存放着内置的函数和异常

当一行代码要使用变量x的值时，Python会到所有可用的名字空间去查找变量，按照如下顺序：
1.局部名字空间 - 特指当前函数或类的方法。如果函数定义了一个局部变量x，Python将使用这个变量，然后停止搜索
2.全局名字空间 - 特指当前的模块。如果模块定义了一个名为x的变量，函数或类，Python将使用这个变量然后停止搜索
3.内置名字空间 - 对每个模块都是全局的。作为最后的尝试，Python将假设x是内置函数或变量
'''


print globals()  #全局变量

print locals()   #局部变量

def testh():
    name = 'hehe'
    print globals()
    print locals()

testh()

class testc(object):
    namec = 'world'

    def __init__(self):
        namei = 'init'
        print globals()
        print locals()

    def testc_1(self):
        namec1 = 'test1'

    print globals()
    print locals()


O = testc()
