#coding=utf8

import __builtin__

print "module name __name__ : ", __name__
print "__builtin__ is __builtins__: ", __builtin__ is __builtins__
print "type(__builtin__): ", type(__builtin__)
print "type(__builtins__): ", type(__builtins__)
print "__builtins__ is __builtin__.__dict__", __builtins__ is __builtin__.__dict__


"""
Python为什么可以直接使用一些内建函数，不用显式的导入它们，比如 str() int() dir() ...？
原因是Python解释器第一次启动的时候 __builtins__ 就已经在命名空间了

__builtins__ 是对内建模块 __builtin__ 的引用，并且有如下两个方面差异：
在主模块中，即没有被其他文件导入。__builtins__是对__builtin__本身的引用，两者是相同的

通过 __builtins__ is __builtin__.__dict__ 猜想：
在非'__main__' 模块中，也就是模块被导入后，__builtins__应该属于 __builtin__.__dict__ 的一部分，是对__builtin__.__dict__ 的引用，而非__builtin__本身，它在任何地方都可见，此时__builtins__的类型是字典。

"""
