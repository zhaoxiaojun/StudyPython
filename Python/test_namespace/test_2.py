#coding=utf8

def f():
    a = 1
    print locals()
    locals()['b'] = 2
    locals()['a'] = 2  #locals是只读的，globals不是 ??
    print a
    print locals()

f()
