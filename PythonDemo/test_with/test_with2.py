#coding=utf8

class Sample:
    def __enter__(self):
        print 'in enter'
        return self

    def __exit__(self, type, value, trace):  #异常抛出时，与之关联的type，value和stack trace传给__exit__()方法，因此抛出的ZeroDivisionError异常被打印出来
        print "type:", type
        print "value:", value
        print "trace:", trace

    def do_something(self):
        bar = 1/1
        print 'bar:',bar
        return bar + 10

with Sample() as sample:
    print sample.do_something()
