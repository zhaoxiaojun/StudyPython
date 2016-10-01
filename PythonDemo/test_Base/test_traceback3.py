#coding=utf8
#原理

def func(a, b):
    return a / b


if __name__ == '__main__':
    import sys
    import traceback
    try:
        func(1, 0)
    except Exception as e:
        print "print_exception()"
        exc_type, exc_value, exc_tb = sys.exc_info()
        print 'the exc type is:', exc_type
        print 'the exc value is:', exc_value
        print 'the exc tb is:', exc_tb
        print '\n'
        for filename, linenum, funcname, source in traceback.extract_tb(exc_tb):
            print "%-23s:%s '%s' in %s()" % (filename, linenum, source, funcname)
        print '\n\n'
        traceback.print_exception(exc_type, exc_value, exc_tb)

#traceback.print_exc()函数只是traceback.print_exception()函数的一个简写形式，而它们获取异常相关的数据都是通过sys.exc_info()函数得到的
#sys.exc_info()返回的值是一个元组，其中第一个元素，exc_type是异常的对象类型，exc_value是异常的值，exc_tb是一个traceback对象，对象中包
#含出错的行数、位置等数据。然后通过print_exception函数对这些异常数据进行整理输出
