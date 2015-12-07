#coding=utf8
import sys
import string

if len(sys.argv) < 2:
   print "NO canshu"
   sys.exit(0)
n = 1
for i in sys.argv[1:]:
     strcanshu = str(i)
     print  'di',n,'ge canshu shi',strcanshu
     n = n + 1
print 'testing'
