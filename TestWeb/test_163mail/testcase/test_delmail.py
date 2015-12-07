#coding=utf-8
from selenium import webdriver
import unittest,time
from public import login
#鼠标操作
from selenium.webdriver.common.action_chains import ActionChains
"""
perform() 执行所有 ActionChains 中存储的行为
context_click() 右击
double_click() 双击
drag_and_drop() 拖动
move_to_element() 鼠标悬停
"""

class TestDelmail(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.baseurl = 'http://mail.163.com/'
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
    def test_163mail_delmail_01(self):
        u'''通过删除按钮进行邮件删除'''
        driver = self.driver
        login.login(driver, self.baseurl, "defias_test", "testing")
        
        #点击收件箱 @class='nui-tree-item-text' and @title=u'收件箱'
        #driver.find_element_by_xpath("html/body/div/nav/div[2]/ul/li/div/span[@class='nui-tree-item-text']").click()
        #driver.find_element_by_xpath("//li[@id='_mail_component_45_45']/span[2]").click()
        #driver.find_element_by_xpath("//div[@id='dvNavTree']/ul/li/div/span[@class='nui-tree-item-text']").click()
        driver.find_element_by_css_selector("div[id='dvNavTree']").find_element_by_css_selector("span[title='收件箱']").click()
        
        
        #选中第一封邮件 /div[@aria-label]
        driver_mail_list = driver.find_element_by_css_selector("div[id$='_ListDiv']").find_elements_by_css_selector("div[sign='letter']")
        driver_mail_list[0].find_element_by_css_selector("b[class$='checkbox']").click()
        '''
        for i in driver_mail_list:
            #i.find_element_by_xpath("div/div/label/span/b").click()
            i.find_element_by_css_selector("b[class$='checkbox']").click()
            break
        '''
        
        #点击删除按钮
        driver.find_element_by_css_selector("header[id$='_Header']").find_element_by_xpath("div/div[2]/div/span").click()
        
        #验证删除成功
        self.assertEqual(u"已删除",driver.find_element_by_css_selector("span.nui-tips-text>a").text)
        
    def test_163mail_delmail_02(self):
        u'''通过点击鼠标右键下拉菜单删除邮件'''
        driver = self.driver
        login.login(driver, self.baseurl, "defias_test", "testing")
        
        #点击收件箱
        driver.find_element_by_css_selector("div[id='dvNavTree']").find_element_by_css_selector("span[title='收件箱']").click()
        
        
        #在第一封邮件上点击鼠标右键
        driver_mail_list = driver.find_element_by_css_selector("div[id$='_ListDiv']").find_elements_by_css_selector("div[sign='letter']")
        menu_mail = driver_mail_list[0].find_element_by_css_selector("b[class$='checkbox']")
        ActionChains(driver).move_to_element(menu_mail).context_click(menu_mail).perform()
   
        #鼠标点击删除选项
        menu_list = driver.find_elements_by_css_selector("div[role='menu']>div[role='menuitem']")
        menu_del = menu_list[4].find_element_by_css_selector(".nui-menu-item-text")
        ActionChains(driver).move_to_element(menu_del).click(menu_del).perform()
        #menu_del.click()
        
        #验证删除成功
        self.assertEqual(u"已删除",driver.find_element_by_css_selector("span.nui-tips-text>a").text)

if __name__ == "__main__":
    unittest.main()
    
    