#coding=utf8
#演示生成器

def genner(n):
    print 111
    for i in range(n):
        print 222
        yield i ** 2


x = genner(5)
print x.next()
print x.next()
print x.next()
print x.next()
print x.next()

# #这样写与上面不等价
# print genner(5).next()
# print genner(5).next()
