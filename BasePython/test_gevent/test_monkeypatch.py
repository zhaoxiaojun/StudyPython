#coding=utf8

class Foo(object):
    def bar(self):
        print 'Foo.bar'

def bar(self):
    print 'Modified bar'

Foo().bar()

Foo.bar = bar

Foo().bar()


def originalFunc():
    print 'this is original function!'

def modifiedFunc():
    modifiedFunc=1
    print 'this is modified function!'

def main():
    originalFunc()

if __name__=='__main__':
    originalFunc=modifiedFunc
    main()
