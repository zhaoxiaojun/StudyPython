#coding=utf8
import sys
import gc

'''
在Python中，每个对象都有存有指向该对象的引用总数，即引用计数(reference count),可以使用sys包中的getrefcount()，来查看某个对象的引用计数
'''
a = [1, 2, 3]
print(sys.getrefcount(a))   #传递给getrefcount()时，参数实际上创建了一个临时的引用。因此，getrefcount()所得到的结果，会比期望的多1

b = a
print(sys.getrefcount(b))


#对象引用对象
class from_obj(object):
    def __init__(self, to_obj):
        self.to_obj = to_obj

b = [1,2,3]
a = from_obj(b)
print(id(a.to_obj))   #内置函数id()用于返回对象的身份(identity) 其实就是该对象的内存地址
print(id(b))


#两个对象可能相互引用,构成引用环
a = []
b = [a]
a.append(b)
print(sys.getrefcount(a))
print(sys.getrefcount(b))


#自己引用自己,也能构成引用环
x = []
x.append(x)
print(sys.getrefcount(x))


#引用减少
a = [1, 2, 3]
b = a
print(sys.getrefcount(b))

del a
print(sys.getrefcount(b))


#引用减少
a = [1, 2, 3]
b = a
print(sys.getrefcount(b))

a = 1
print(sys.getrefcount(b))


'''
减肥(垃圾回收)是个昂贵而费力的事情。垃圾回收时，Python不能进行其它的任务。频繁的垃圾回收将大大降低Python的工作效率。如果内存中的对象不多，就没有必要总启动垃圾
回收。所以，Python只会在特定条件下，自动启动垃圾回收。当Python运行时，会记录其中分配对象(object allocation)和取消分配对象(object deallocation)的次数。当两者的
差值高于某个阈值时，垃圾回收才会启动。
'''
print(gc.get_threshold())  #通过gc模块的get_threshold()方法，查看该阈值
#(700, 10, 10)
#第一个值（700）：即是垃圾回收启动的阈值。
#gc.set_threshold(700, 10, 5)  #可以通过gc中的set_threshold()方法重新设置
#gc.collect()   #手动启动垃圾回收



'''
Python同时采用了分代(generation)回收的策略。这一策略的基本假设是，存活时间越久的对象，越不可能在后面的程序中变成垃圾。我们的程序往往会产生大量的对象，许多对象
很快产生和消失，但也有一些对象长期被使用。出于信任和效率，对于这样一些“长寿”对象，我们相信它们的用处，所以减少在垃圾回收中扫描它们的频率。

Python将所有的对象分为0，1，2三代。所有的新建对象都是0代对象。当某一代对象经历过垃圾回收，依然存活，那么它就被归入下一代对象。垃圾回收启动时，一定会扫描所有的
0代对象。如果0代经过一定次数垃圾回收，那么就启动对0代和1代的扫描清理。当1代也经历了一定次数的垃圾回收后，那么会启动对0，1，2，即对所有对象进行扫描。
'''
print(gc.get_threshold())
#(700, 10, 10)
#后两个值：每10次0代垃圾回收，会配合1次1代的垃圾回收；而每10次1代的垃圾回收，才会有1次的2代垃圾回收



'''
引用环的存在会给上面的垃圾回收机制带来很大的困难。这些引用环可能构成无法使用，但引用计数不为0的一些对象。
'''
#孤立的引用环
a = []
b = [a]
a.append(b)

del a
del b
#删除了a，b引用之后，这两个对象不可能再从程序中调用，就没有什么用处了。但是由于引用环的存在，这两个对象的引用计数都没有降到0，不会被垃圾回收。

'''
“标记-清除”是为了解决循环引用的问题
'''
