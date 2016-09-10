#coding=utf8

def genn():
    lst = [1,2,3]
    try:
        for i in lst:
            yield i
        print 1111
        raise
    except:
        lst = [1, 2, 3]

go = genn()
print go.next()
print go.next()
print go.next()
print go.next()
