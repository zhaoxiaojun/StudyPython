#coding=utf8
#异常用法

import sys
import traceback

#----------------
#sys.exc_info()[2].tb_lineno值不是固定的
try:
    x=1/0
except Exception as e:
    print "Exception:[%s][%s]" % (sys.exc_info()[2].tb_lineno, str(e))
finally:
    print "This is finally "

#----------------
try:
    raise Exception("HAHAHA")
except Exception as e:
    print "Exception:[%s][%s]" % (sys.exc_info()[2].tb_lineno, str(e))

#----------------
try:
    1/0
except ZeroDivisionError:
    print 'aaaaaaaaaaaa'
except:
    print 'bbbbbbbbbbb'

#----------------
try:
    x=1/0
except Exception as e:
    print "Exception:[%s][%s]" % (sys.exc_info()[2].tb_lineno, str(e))


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

traceback_template = '''Traceback (most recent call last):
 File "%(filename)s", line %(lineno)s, in %(name)s
%(type)s: %(message)s\n''' # Skipping the "actual line" item


try:
    x=1/0
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback_details = {
            'filename': exc_traceback.tb_frame.f_code.co_filename,
            'lineno' : exc_traceback.tb_lineno,
            'name'  : exc_traceback.tb_frame.f_code.co_name,
            'type'  : exc_type.__name__,
            'message' : exc_value.message, # or see traceback._some_str()
    }
    print traceback_template % traceback_details
