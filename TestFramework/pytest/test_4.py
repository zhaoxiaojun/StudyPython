#coding=utf-8

class TestClass(object):

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert x == "hi"


'''
当前目录下执行：

生成普通的测试结果日志文件：
py.test test_4.py  --resultlog=./log_4.txt

生成JunitXML测试结果日志文件：
py.test test_4.py  --junitxml=./log_4.xml

生成测试结果日志文件的URL（获得一个展示结果的url，如：https://bpaste.net/show/d6a9a5e79c4c）：
py.test test_4.py  --pastebin=all
py.test test_4.py  --pastebin=failed #只选择展示faile的测试用例
（mac上要把代理关掉，否则报错）

生成测试结果日志文件html测试报告：
py.test test_4.py --html=./report_4.html

'''
