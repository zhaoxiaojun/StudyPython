#coding=utf-8
from selenium import webdriver
import unittest,time,os
from public import login
#键盘
from selenium.webdriver.common.keys import Keys
#显示等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestSendmail(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)    #隐式等待
        self.baseurl = 'http://mail.163.com/'
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.driver.quit()
        self.assertEqual(self.verificationErrors, [])
    
    def test_163mail_sendmail_01(self):
        u'''只输入收件人进行发送邮件'''
        driver = self.driver
        #登录
        login.login(driver, self.baseurl, 'defias_test', 'testing')
        
        #点击写信按钮
        driver.find_element_by_css_selector("#dvNavTop").find_element_by_xpath("ul/li[2]/span[2]").click()
        
        #输入收件人信息
        driver.find_element_by_css_selector("input.nui-editableAddr-ipt").clear()
        driver.find_element_by_css_selector("input.nui-editableAddr-ipt").send_keys("defias_test@163.com")
        driver.find_element_by_css_selector("input.nui-editableAddr-ipt").send_keys(Keys.ENTER)
        
        #点击发送按钮
        #driver.find_element_by_xpath("html/body/div[2]/div/div[2]/header/div/div/div/span[2]").click()
        button_list = driver.find_element_by_css_selector(".frame-main-outer").find_elements_by_css_selector(".nui-toolbar-item")
        button_list[0].find_element_by_css_selector(".nui-btn-text").click()
        
        #点击确定按钮 弹出窗处理
        driver.switch_to_active_element().send_keys(Keys.ENTER)   #通过键盘回车确定，如何通过鼠标点击确定？
        
        #显示等待
        '''
        for unused_i in range(60):
            try:
                if u"发送成功" == driver.find_element_by_css_selector("h1[id$='_succInfo']").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        '''
        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"h1[id$='_succInfo']"),u"发送成功"))
        
        #断言
        self.assertEqual(u"发送成功", driver.find_element_by_css_selector("h1[id$='_succInfo']").text)
    
    def test_163mail_sendmail_02(self):
        u'''只输入收信人与主题发送邮件'''
        driver = self.driver
        #登录
        login.login(driver, self.baseurl, 'defias_test', 'testing')
        
        #点击写信按钮
        driver.find_element_by_css_selector("#dvNavTop").find_element_by_xpath("ul/li[2]/span[2]").click()
        
        #输入收件人信息
        driver.find_element_by_css_selector("input.nui-editableAddr-ipt").clear()
        driver.find_element_by_css_selector("input.nui-editableAddr-ipt").send_keys("defias_test@163.com")
        driver.find_element_by_css_selector("input.nui-editableAddr-ipt").send_keys(Keys.ENTER)
        
        #输入主题信息
        driver.find_element_by_css_selector("div[aria-label='邮件主题输入框，请输入邮件主题']>input").clear()
        driver.find_element_by_css_selector("div[aria-label='邮件主题输入框，请输入邮件主题']>input").send_keys(u"test测试")
        
        #点击发送按钮
        button_list = driver.find_element_by_css_selector(".frame-main-outer").find_elements_by_css_selector(".nui-toolbar-item")
        button_list[0].find_element_by_css_selector(".nui-btn-text").click()
        
        #点击确定按钮
        driver.switch_to_active_element().send_keys(Keys.ENTER)   #通过键盘回车确定，如何通过鼠标点击确定？
        
        #显示等待
        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"h1[id$='_succInfo']"),u"发送成功"))
        
        #断言
        self.assertEqual(u"发送成功", driver.find_element_by_css_selector("h1[id$='_succInfo']").text)
        
    def test_163mail_sendmail_03(self):
        u'''输入收信人、主题和正文发送邮件'''
        driver = self.driver
        #登录
        login.login(driver, self.baseurl, 'defias_test', 'testing')
        
        #点击写信按钮
        driver.find_element_by_css_selector("#dvNavTop").find_element_by_xpath("ul/li[2]/span[2]").click()
        
        #输入收件人信息
        driver.find_element_by_css_selector("input.nui-editableAddr-ipt").clear()
        driver.find_element_by_css_selector("input.nui-editableAddr-ipt").send_keys("defias_test@163.com")
        driver.find_element_by_css_selector("input.nui-editableAddr-ipt").send_keys(Keys.ENTER)
        
        #输入主题信息
        driver.find_element_by_css_selector("div[aria-label='邮件主题输入框，请输入邮件主题']>input").clear()
        driver.find_element_by_css_selector("div[aria-label='邮件主题输入框，请输入邮件主题']>input").send_keys(u"test测试")
        
        #输入邮件正文信息 
        driver.find_element_by_css_selector("div[aria-label='邮件主题输入框，请输入邮件主题']>input").send_keys(Keys.TAB)
        #表单切换，切换到APP-editor-iframe
        driver.switch_to_frame(driver.find_element_by_class_name('APP-editor-iframe'))                              
        driver.find_element_by_class_name('nui-scroll').send_keys(u"我是邮件正文，I am mail contain")
        #切换回默认frame
        driver.switch_to_default_content()
        
        #点击发送按钮
        button_list = driver.find_element_by_css_selector(".frame-main-outer").find_elements_by_css_selector(".nui-toolbar-item")
        button_list[0].find_element_by_css_selector(".nui-btn-text").click()
        
        #显示等待发送成功
        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"h1[id$='_succInfo']"),u"发送成功免费短信通知"))
        
        #断言
        self.assertEqual(u"发送成功免费短信通知", driver.find_element_by_css_selector("h1[id$='_succInfo']").text)   
        
    def test_163mail_sendmail_04(self):
        u'''输入收信人、主题和附件发送邮件'''
        driver = self.driver
        #登录
        login.login(driver, self.baseurl, 'defias_test', 'testing')
        
        #点击写信按钮
        driver.find_element_by_css_selector("#dvNavTop").find_element_by_xpath("ul/li[2]/span[2]").click()
        
        #输入收件人信息
        driver.find_element_by_css_selector("input.nui-editableAddr-ipt").clear()
        driver.find_element_by_css_selector("input.nui-editableAddr-ipt").send_keys("defias_test@163.com")
        driver.find_element_by_css_selector("input.nui-editableAddr-ipt").send_keys(Keys.ENTER)
        
        #输入主题信息
        driver.find_element_by_css_selector("div[aria-label='邮件主题输入框，请输入邮件主题']>input").clear()
        driver.find_element_by_css_selector("div[aria-label='邮件主题输入框，请输入邮件主题']>input").send_keys(u"test测试")
        
        #输入邮件正文信息 
        driver.find_element_by_css_selector("div[aria-label='邮件主题输入框，请输入邮件主题']>input").send_keys(Keys.TAB)
        driver.switch_to_frame(driver.find_element_by_class_name('APP-editor-iframe'))  #切换frame
        driver.find_element_by_class_name('nui-scroll').send_keys(u"我是邮件正文，I am mail contain")
        driver.switch_to_default_content()  #切换回默认frame
        
        #附件上传
        #点击上传按钮
        driver.find_element_by_css_selector(".O0").click()
        #调用autoit脚本
        os.system(r"E:\Code\yzhselenium\test_163mail\testcase\tools\upfile.exe")
        
        #点击发送按钮
        button_list = driver.find_element_by_css_selector(".frame-main-outer").find_elements_by_css_selector(".nui-toolbar-item")
        button_list[0].find_element_by_css_selector(".nui-btn-text").click()
        
        #显示等待发送成功
        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"h1[id$='_succInfo']"),u"发送成功免费短信通知"))
        
        #断言
        self.assertEqual(u"发送成功免费短信通知", driver.find_element_by_css_selector("h1[id$='_succInfo']").text)   
        
if __name__ == '__main__':
    unittest.main()
