#coding=utf8
#整洁的打印数据
import pprint

tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead', ('parrot', ('fresh fruit',))))))))

stuff = ['a' * 10, tup, ['a' * 30, 'b' * 30], ['c' * 20, 'd' * 20]]

pprint.pprint(stuff)

#pprint.pprint(stuff, depth=3)

#pprint.pprint(stuff, width=60)
