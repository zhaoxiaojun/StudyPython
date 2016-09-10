#coding=utf8
#生成器也是一种迭代器。生成器拥有next方法并且行为与迭代器完全相同，这意味着生成器也可以用于Python的for循环中
#生成器是一种特殊的迭代器，内部支持了生成器协议，不需要明确定义__iter__()和next()方法
#生成器可以通过生成器函数产生，生成器函数可以通过常规的def语句来定义，但是不用return返回，而是用yield一次返回一个结果

#创建生成器方式1：
lst = [1,2,3,4,5,6]
o = (x+1 for x in lst) #生成器表达式

print o

print o.next()
print o.next()
print o.next()
# print o.send(None)
# print o.send(1)
print o.next()
print o.next()
print o.next()

o = (x+1 for x in lst)
print o.next()
