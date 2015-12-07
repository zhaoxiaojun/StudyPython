#coding=utf8
import sys

def get_cur_info():
    print sys._getframe().f_code.co_name
    print sys._getframe().f_back.f_code.co_name
    print sys._getframe().f_lineno

get_cur_info()
