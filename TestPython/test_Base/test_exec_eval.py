#coding=utf8

#exec('print(x)', {"x": "abc"})

#print(eval('x*2', {"x": 5}))


class MyError(Exception):
    '''
    自定义异常类
    '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    print 11111
    table = 'name'
    raise  MyError(u"%s" % table)
except MyError as e:
    print 22222
    print unicode(e)
except Exception as e:
    print 33333


print '---------'
