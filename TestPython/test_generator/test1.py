#coding=utf8
#演示生成器

def genner(n):
    for i in range(n):
        yield i ** 2
x = genner(5)
print x.next()
print x.next()
print x.next()
print x.next()
print x.next()
