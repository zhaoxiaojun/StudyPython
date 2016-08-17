#encoding: utf-8

"""
在特殊情况的下才会使用reload函数；除了原来模块文件有修改外，还有哪些情况需要使用reload函数呢，例子:
"""
import sys   #引用sys模块进来，并不是进行sys的第一次加载
reload(sys)  #重新加载sys
sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数  如果不重新加载sys该条语句会执行失败




"""
为什么要在调用setdefaultencoding时必须要先reload一次sys模块呢？
因为这里的import语句其实并不是sys的第一次导入语句，也就是说这里其实可能是第二、三次进行sys模块的import，这里只是一个对sys的引用，
只能reload才能进行重新加载；

那么为什么要重新加载，而直接引用过来则不能调用该函数呢？
因为setdefaultencoding函数在被系统调用后被删除了，所以通过import引用进来时其实已经没有了，所以必须reload一次sys模块，这样
setdefaultencoding才会为可用，才能在代码里修改解释器当前的字符编码
"""
