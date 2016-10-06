#coding=utf-8
from counter import counter
#没有使用测试框架，写测试相当的麻烦



class test_counter:
    def test_add1(self):
        try:
            add = counter()
            vadd = add.add(1,9)
            assert(10 == vadd),'test fail!'
        except AssertionError,msg:
            print msg
        else:
            print 'test pass!'

    def test_subtraction1(self):
        try:
            add = counter()
            vadd = add.subtraction(100, 1)
            assert(99 == vadd),'test fail!'
        except AssertionError,msg:
            print msg
        else:
            print 'test pass!'

#执行测试类的测试方法
mytest = test_counter()
mytest.test_add1()
mytest.test_subtraction1()
