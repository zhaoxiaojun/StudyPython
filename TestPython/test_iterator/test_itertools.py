#coding=utf8
import itertools
'''
提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算
'''

natuals = itertools.count(1)  #无限的迭代器:自然数序列
#!!!
#for n in natuals:
#    print(n)
ns = itertools.takewhile(lambda x: x <= 10, natuals)   #通过takewhile()等函数根据条件判断来截取出一个有限的序列
print ns
print list(ns)


cs = itertools.cycle('ABC')     #把传入的一个序列无限重复下去  注意字符串也是序列的一种
#!!!
#for c in cs:
#    print(c)


ns = itertools.repeat('A', 3)   #负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
for n in ns:
    print(n)
print '\n----------------------\n'


for c in itertools.chain('ABC', 'XYZ'):     #把一组迭代对象串联起来，形成一个更大的迭代器
    print(c)
print '\n----------------------\n'


for key, group in itertools.groupby('AAABBBCCAAA'):     #把迭代器中相邻的重复元素挑出来放在一起
    #print key
    #print group
    #print 'type(key):',type(key)
    #print 'type(group):', type(group)
    print(key, list(group))
print '\n----------------------\n'


'''
实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，
而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key
'''
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))
