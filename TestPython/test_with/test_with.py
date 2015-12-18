#coding=utf8

with open("foo.txt") as file:
    data = file.read()
print data
print '\n---------------------\n'


class Sample:
    def __enter__(self):
        print "In \n__enter__()"
        return "Foo"

    def __exit__(self, type, value, trace):
        print "In \n__exit__()"

def get_sample():
    return Sample()


with get_sample() as sample:
    print "sample:",sample
'''
紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。当with后面的代码块全部被执行完之后，将调用前面返回对象
的__exit__()方法：
1. __enter__()方法被执行
2. __enter__()方法返回的值 - 这个例子中是"Foo"，赋值给变量'sample'
3. 执行代码块，打印变量"sample"的值为 "Foo"
4. __exit__()方法被调用
'''
print '\n-------------------\n'



class Sample:
    def __enter__(self):
        print 'in enter'
        return self

    def __exit__(self, type, value, trace):
        print "type:", type
        print "value:", value
        print "trace:", trace

    def do_something(self):
        bar = 1/1
        print 'bar:',bar
        return bar + 10

def testtt():
    with Sample() as sample:    #with后面的get_sample()变成了Sample()。这没有任何关系，只要紧跟with后面的语句所返回的对象有__enter__()和__exit__()方法即可
        return sample.do_something()

testtt()
'''
异常抛出时，与之关联的type，value和stack trace传给__exit__()方法，因此抛出的ZeroDivisionError异常被打印出来
'''

'''
用途:
开发库时，清理资源，关闭文件等等操作，都可以放在__exit__方法当中
Python的with语句是提供一个有效的机制，让代码更简练，同时在异常产生时，清理工作更简单
'''
