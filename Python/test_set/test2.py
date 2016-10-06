#coding=utf8

#去除海量列表里重复元素
a = [11,22,33,44,11,22]
b = set(a)
print b

s = set([3,5,9,10])      #创建一个数值集合

t = set("Hello")         #创建一个字符的集合

x = 1


t.add('x')            #添加一项
print t

s.update([10,37,42])  #在s中添加多项
print s

t.remove('H')  #删除一项
print t

s.discard(x)   #如果在s中存在元素x, 则删除
print s

s.pop()  #删除并且返回s中的一个不确定的元素, 如果为空则引发KeyError
print s

#s.clear()  #删除s中的所有元素


print len(s)   #set的长度


print x in s  #测试x是否是s的成员

print x not in s   #测试x是否不是s的成员

#测试是否 s 中的每一个元素都在 t 中
print s.issubset(t)
print s <= t

#测试是否 t 中的每一个元素都在 s 中
print s.issuperset(t)
print s >= t


print s.copy()  #s的一个浅复制


