#coding=utf8
import sys
import getopt

print sys.argv


opts, args = getopt.getopt(sys.argv[1:], "h:p:", ["help", "host=", "port="])

print 'opts: ',opts
print 'args: ',args
