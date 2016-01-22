#coding=utf-8
#异常用法

import sys

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

