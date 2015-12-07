#coding=utf8
#演示文档字符串
'''I am this file's doc string,hehe!'''

def prt(x,y):
    '''I am doc string!
I hope you can remeber me'''

    '''I am testing'''

    print x,y  #I am tip too,please remeber I am diferent in version 3.0

prt(1,2)
print prt.__doc__

import sys
print sys.__doc__

import if_exp
print if_exp.__doc__

