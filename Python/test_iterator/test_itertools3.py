#coding=utf8
import itertools

listone = ['a','b','c']
listtwo = ['11','22','abc']

def funLargeFive(x):
    if x > 5:
        return True

for item in itertools.ifilter(funLargeFive,range(-10,10)):
    '''
    返回一个可以让fun返回True的迭代器
    ifilter(pred, seq)  内建函数filter的迭代器版本
    '''
    print item,

print '\n---------------------------\n'

listone = ['a','b','c']
listtwo = ['11','22','abc']
listthree = [1,2,3]

def funAddFive(x):
    return x + 5

for item in itertools.imap(funAddFive,listthree):
    '''
    返回一个迭代器，对iterator中的每个项目调用fun
    imap(func, p, q, ...)  内建函数map的迭代器版本
    '''
    print item,


print '\n---------------------------\n'


listone = ['a','b','c']
listtwo = ['11','22','abc']
listthree = listone + listtwo
for item in itertools.islice(listthree,3,5):   #返回迭代器，其中的项目来自将seq从start开始到stop结束以step步长切割后d的 islice(seq, [start,] stop [, step])
    print item,

print '\n---------------------------\n'


listone = ['a','b','c']
listtwo = ['11','22','abc']
listthree = listone + listtwo
for item in itertools.izip(listone,listtwo):
    '''
    返回迭代器，项目是元组，元组来自*iterator的组合 izip(*iterator)
    izip(p, q, ...)   内建函数zip的迭代器版本
    '''
    print item,

print '\n---------------------------\n'

a = "hello"
c, d = itertools.tee(iter(a), 2)
'''
tee(it[, n = 2]) 把一个迭代器分为n个迭代器, 返回一个元组, 默认是两个
tee(it, n)  返回n个迭代器it的复制迭代器
'''
for i, j in zip(c, d):
    print i, j
