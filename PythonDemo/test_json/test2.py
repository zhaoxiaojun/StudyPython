#coding=utf8
import json

#对dict对象进行排
data1 = {'b':789,'c':456,'a':123}
data2 = {'a':123,'b':789,'c':456}
d1 = json.dumps(data1,sort_keys=True)
d2 = json.dumps(data2)
d3 = json.dumps(data2,sort_keys=True)
print d1
print d2
print d3
print d1==d2
print d1==d3


#使数据存储的格式变得更加优雅
data1 = {'b':789,'c':456,'a':123}
d1 = json.dumps(data1,sort_keys=True,indent=4)
print d1



"""
输出的数据被格式化之后，变得可读性更强，但是却是通过增加一些冗余的空白格来进行填充的。json主要是作为一种数据通信的格式存在的，而网络通信是很在乎数据的
大小的，无用的空格会占据很多通信带宽，所以适当时候也要对数据进行压缩。separator参数可以起到这样的作用，该参数传递是一个元组，包含分割对象的字符串
"""
data = {'b':789,'c':456,'a':123}
print 'DATA:', repr(data)
print 'repr(data)             :', len(repr(data))
print 'dumps(data)            :', len(json.dumps(data))
print 'dumps(data, indent=2)  :', len(json.dumps(data, indent=4))
print 'dumps(data, separators):', len(json.dumps(data, separators=(',',':')))



"""
另一个比较有用的dumps参数是skipkeys，默认为False。 dumps方法存储dict对象时，key必须是str类型，如果出现了其他类型的话，那么会产生TypeError异常，
如果开启该参数，设为True的话，则会比较优雅的过度。
"""
data = {'b':789,'c':456,(1,2):123}
print json.dumps(data,skipkeys=True)
