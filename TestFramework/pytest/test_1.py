#coding=utf-8

#功能
def func(x):
    return x + 1


#测试用例
def test_answer():
    assert func(3) == 5


'''
当前目录下执行： py.test

pytest是如果识别测试用例的呢？
它默认使用检查以test_ *.py 或*_test.py命名的文件名，在文件内部查找以test_打头的方法或函数，并执行它们
'''

