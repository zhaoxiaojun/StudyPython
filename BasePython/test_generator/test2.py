#coding=utf8

class genn(object):
    def __init__(self, n):
        self.n = n

    def genner(self):
        print 'ing'
        for i in range(self.n):
            yield i ** 2

go = genn(5)
xo = go.genner()

print xo.next()
print xo.next()
print xo.next()
print xo.next()
print xo.next()
