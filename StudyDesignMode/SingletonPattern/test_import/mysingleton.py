#coding=utf8
#python的模块是天然的单例模式


class my_singleton(object):
    def foo(self):
        print 'foo'

my_singletonO = my_singleton()
