#coding=utf8
import traceback

class myError(IOError):
    """123456789"""
    pass

def function1():
    function2()

def function2():
    function3()

def function3():
    try:
        #raise myError,('my exception',"abxc")
        assert 1 == 0,u'断言错误'
    except StandardError:
        print 'Caught exception in function3.Rearaising......\n'
        raise
    except:
        print '111111'
        raise


try:
    function1()

except Exception,kkk:
    print "Exception caught in main program."
    print '\nkkk type: %s' % type(kkk)
    print "\nExceptin argments: %s" % unicode(kkk.args[0])
    print "\nExceptin argments type:", type(kkk.args[0])
    #print "\nException message:",kkk
    print "\nTraceback:"
    traceback.print_exc()


