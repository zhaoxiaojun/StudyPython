#coding=utf8
#python的魔法方法

"""
基本定制
C.__init__(self[, arg1, ...]) 构造器（带一些可选的参数）
C.__new__(self[, arg1, ...]) 构造器（带一些可选的参数）；通常用在设置不变数据类型的子类
C.__del__(self) 解构器
C.__str__(self) 可打印的字符输出；内建str()及print 语句
C.__repr__(self) 运行时的字符串输出；内建repr()  ‘‘  和 操作符
C.__unicode__(self)b Unicode 字符串输出；内建unicode()
C.__call__(self, *args) 表示可调用的实例
C.__nonzero__(self) 为object 定义False 值；内建bool() （从2.2 版开始）
C.__len__(self) “ ” 长度（可用于类）；内建len()
"""

class A(object):
    def __new__(self):
        print "call __new__"

    def __init__(self):
        print "call __init__"
        self.a = 1

    def __del__(self):
        print "call __del__"

    def __str__(self):
        print "call __str__"
        return "class A str"

    def __repr__(self):
        print "call __repr__"
        return "class A repr"

    def __unicode__(self):
        print "call __unicode__"
        return "class A unicode"

    def __nozero__(self):
        print "call __nozero__"
        return 1

    def __len__(self):
        print "call __len__"
        return 1

    def __call__(self, *args):   #定义后执行：callable(instance) 为True
        print "call __call__"


a = A()
print a
#repr(a)
#unicode(a)
#print bool(a)
#print len(a)
#print callable(a)
