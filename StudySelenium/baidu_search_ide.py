# -*- coding: utf-8 -*-
#由selenium IDE导出的python2/unittest/webdriver脚本
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re    #导入相关模块包括unittest框架

class BaiduSearchIde(unittest.TestCase):    #继承框架类unittest.TestCase
    #设置环境初始化工作，在每个用例前被执行
    def setUp(self):
        self.driver = webdriver.Firefox()        #启动firefox浏览器
        self.driver.implicitly_wait(30)          #设置整个页面的隐性等待时间
        self.base_url = "https://www.baidu.com/"  #URL地址
        self.verificationErrors = []         #脚本运行时的错误信息保存到该数组中
        self.accept_next_alert = True        #是否继续接受下一个警告
    
    def test_baidu_search_ide(self):         #测试方法
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium ide")
        driver.find_element_by_id("su").click()
        # 断言
        for i in range(60):                  #waitForTitle
            try:
                if u"selenium ide_百度搜索" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")          #循环结束超时
        self.assertEqual(u"selenium ide_百度搜索", driver.title)  #断言
    
    def is_element_present(self, how, what):               #查找页面元素是否存在
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):                            #处理弹出的告警框
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):                #关闭告警并获得告警信息
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    #设置环境清理工作，在每个用例执行后执行
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()                #通过框架的main方法执行测试用例，默认执行以test开头的方法
