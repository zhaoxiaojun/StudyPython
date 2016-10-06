#coding=utf8

class TestUM():
    def setup(self):
        print('setup方法执行于本类中每条用例之前')

    def teardown(self):
        print('teardown方法执行于本类中每条用例之后')

    @classmethod  #必须的
    def setup_class(cls):
        print('setup_class类方法执行于本类中任何用例开始之前,且仅执行一次')

    @classmethod  #必须的
    def teardown_class(cls):
        print('teardown_class类方法执行于本类中所有用例结束之后,且仅执行一次')

    def test_strings(self):
        assert 'a' * 3 =='aaa'

    def test_ints(self):
        assert 3 * 3 == 9



'''
class的setup 、teardown的设置
setup函数的取名可以是setup_class, setupClass, setUpClass, setupAll ,setUpAll中的一个
teardown函数取名可以是teardown_class, teardownClass, tearDownClass, teardownAll ,tearDownAll中的一个
测试类也可以继承unittest.TestCase
'''
