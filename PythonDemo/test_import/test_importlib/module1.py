#coding=utf8

def funcA12():
    print('funcA12 in module1')
    return


import os
print  os.path.join(os.path.abspath(os.path.dirname(__file__)),('templates'))
