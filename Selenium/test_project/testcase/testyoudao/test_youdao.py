# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time

class TestYoudaoSearch(unittest.TestCase):    #继承框架类unittest.TestCase
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        self.driver = webdriver.Chrome(chrome_options=options)        #启动Chrome浏览器
        self.driver.maximize_window()            #窗口最大化
        self.driver.implicitly_wait(10)          #设置整个页面的隐性等待时间
        self.base_url = "https://www.youdao.com/"  #URL地址

    
    def test_youdao_search(self):         #测试方法
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("query").clear()
        driver.find_element_by_id("query").send_keys("test youdao")
        driver.find_element_by_id("qb").click()
        
        time.sleep(3)
        self.assertEqual(u"test youdao - 有道搜索", driver.title)  #断言
    
    def ytest_youdao_search2(self):         #测试方法
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("query").clear()
        driver.find_element_by_id("query").send_keys(u"搜索中文")
        driver.find_element_by_id("qb").click()
        
        time.sleep(3)
        self.assertEqual(u"搜索中文 - 有道搜索", driver.title)  #断言
    
    def ytest_youdao_search3(self):         #测试方法
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("query").clear()
        driver.find_element_by_id("query").send_keys(u"搜索繁體")
        driver.find_element_by_id("qb").click()
        
        time.sleep(3)
        print 'driver.title:',driver.title
        self.assertEqual(u"搜索繁体 - 有道搜索", driver.title)  #断言
           
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    #以test开头的测试方法默认已经加入到测试套中
    #test_suite.addTest(TestYoudaoSearch("test_youdao_search"))
    #test_suite.addTest(TestYoudaoSearch("test_youdao_search2"))
    #test_suite.addTest(TestYoudaoSearch("test_youdao_search3"))
    unittest.TextTestRunner().run(test_suite)
    