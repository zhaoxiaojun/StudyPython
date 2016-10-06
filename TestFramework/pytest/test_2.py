#coding=utf-8

class TestClass(object):

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert x == "hi"

'''
当前目录下执行： py.test -q test_2.py

-q  为quiet。表示在安静的模式输出报告(输出信息相比不带该参数会少一点)
'''
