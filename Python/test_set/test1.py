#coding=utf8

#集合运算

s = set([1,2,3])

t = set([1,4,5])


a = t | s          # t 和 s的并集 s.union(t)
print a

b = t & s          # t 和 s的交集 s.intersection(t)
print b

c = t - s          # 求差集（项在t中，但不在s中）  s.difference(t)
print c

d = t ^ s          # 对称差集（项在t或s中，但不会同时出现在二者中）  s.symmetric_difference(t)
print d


s |= t
print s



