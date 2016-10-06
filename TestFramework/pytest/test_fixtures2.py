#coding=utf-8
import pytest



# 功能函数
def multiply(a,b):
    return a * b

class TestUM:

    # =====fixtures========
    def setup(self):
        print ("setup----->")

    def teardown(self):
        print ("teardown-->")

    def setup_class(cls):
        print ("\n")
        print ("setup_class=========>")

    def teardown_class(cls):
        print ("teardown_class=========>")

    def setup_method(self, method):
        print ("setup_method----->>")

    def teardown_method(self, method):
        print ("teardown_method-->>")

    # =====测试用例========
    def test_numbers_5_6(self):
        print 'test_numbers_5_6'
        assert multiply(5,6) == 30

    def test_strings_b_2(self):
        print 'test_strings_b_2'
        assert multiply('b',2) == 'bb'

if __name__ == '__main__':
    pytest.main("-s test_fixtures2.py")



'''
setup_class/teardown_class  在当前测试类的开始与结束执行
setup/treadown                   在每个测试方法开始与结束执行
setup_method/teardown_method     在每个测试方法开始与结束执行，与setup/treadown级别相同
'''
