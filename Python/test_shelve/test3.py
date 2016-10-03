#coding=utf8
import shelve


#潜在的小问题
s = shelve.open('test.dat')

s['x'] = ['a', 'b', 'c']

s['x'].append('d')

print s['x']


#解决的办法
temp = s['x']

temp.append('e')

s['x'] = temp

print s['x']
