#coding=utf8

def testfunc():
    a = 1
    b = 2
    assert a == b


def testfunc2():
    a = 1
    b = 1
    assert a == b



"""
当前目录下执行：
nosetests  或
nosetests test2_1  或
nosetests test2_1.py

或

上层目录执行：
nosetests  test2  或
nosetests test2/test2_1  或
nosetests test2/test2_1.py

或

python -m nose test2_1.py

"""
