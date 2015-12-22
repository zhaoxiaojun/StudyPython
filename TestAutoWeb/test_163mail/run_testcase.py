#coding=utf-8
import unittest,time
import HTMLTestRunner

#测试用例存放目录
test_dir = r"E:\Code\yzhselenium\test_163mail\testcase"

#自动发现测试用例并生成测试套
test_list = unittest.defaultTestLoader.discover(test_dir, 'test_login.py',  test_dir)

#获取当前时间
now = time.strftime("%Y-%m-%d %H-%M-%S")

#测试报告存放路径
report_path = r"E:\Code\yzhselenium\test_163mail\report\result" + now + ".html"

if __name__ == "__main__":
    fp = file(report_path, 'wb')
    report_runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：' )
    report_runner.run(test_list)
    fp.close()