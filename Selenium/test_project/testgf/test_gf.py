#coding=utf-8
from selenium import webdriver
import unittest
import time

class TestGfSearch(unittest.TestCase):    #继承框架类unittest.TestCase
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        self.driver = webdriver.Chrome(chrome_options=options)        #启动Chrome浏览器
        self.driver.maximize_window()            #窗口最大化
        self.driver.implicitly_wait(10)          #设置整个页面的隐性等待时间
        self.base_url = "http://www.gfsoso.net"  #URL地址

    
    def test_Gf_search(self):         #测试方法
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("lst-ib").clear()
        driver.find_element_by_id("lst-ib").send_keys(u"谷粉")
        driver.find_element_by_xpath('html/body/div[1]/div[2]/center/div[3]/form/div/input[2]').click()
        
        time.sleep(3)
        self.assertEqual(u"谷粉_谷粉搜搜", driver.title)  #断言
    
    def ytest_Gf_search2(self):         #测试方法
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("lst-ib").clear()
        driver.find_element_by_id("lst-ib").send_keys(u"Einglish")
        driver.find_element_by_xpath('html/body/div[1]/div[2]/center/div[3]/form/div/input[2]').click()
        
        time.sleep(3)
        self.assertEqual(u"Einglish_谷粉搜搜", driver.title)  #断言
    
    def ytest_Gf_search3(self):         #测试方法
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("lst-ib").clear()
        driver.find_element_by_id("lst-ib").send_keys(u"搜索繁體")
        driver.find_element_by_xpath('html/body/div[1]/div[2]/center/div[3]/form/div/input[2]').click()
        
        time.sleep(3)
        self.assertEqual(u"搜索繁體_谷粉搜搜", driver.title)  #断言
           
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestSuite())
    