#coding=utf-8
from selenium import webdriver
import unittest,time

#发送指令到远程服务器控制浏览器
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestBaiduSearch(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.baseurl = 'http://www.baidu.com/'
        self.verificationErrors = []
        self.accept_next_alert = True
        #self.driver = webdriver.Firefox()
        #self.driver.implicitly_wait(30)
        self.browser_list = {'http://127.0.0.1:4444/wd/hub':'firefox',
                             'http://127.0.0.1:5555/wd/hub':'chrome'}
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        #self.driver.quit()
        #self.assertEqual([], self.verificationErrors)

    def test_baidu_search_english(self):
        u'''搜索英文'''
        for host,browser in self.browser_list.items():
            print host,browser
            driver = Remote(
                command_executor=host,
                desired_capabilities={
                    'platform':'ANY',
                    'browserName':browser,
                    'version':'',
                    'javascriptEnabled':True
                }
            )
            driver.get(self.baseurl)  #访问url
            driver.find_element_by_id("kw").send_keys(u"selenium")    #搜索框输入
            driver.find_element_by_id("su").click()    #点击搜索按钮
            time.sleep(1)
            assert(u"selenium_百度搜索" == driver.title),'Test Rusult:Fail'     #断言结果
            driver.quit()
            print time.ctime()
            
if __name__ == '__main__':
    unittest.main()
    
        