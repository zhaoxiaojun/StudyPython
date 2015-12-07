#coding=utf-8
from selenium import webdriver
import unittest
#导入公共函数文件
from public import login
from tools import ExcelRW

class TestLogin(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)     #设置整个页面的隐性等待时间
        self.base_url = "http://mail.163.com/"
        self.verificationErrors = []      #错误信息保存数组
        self.accept_next_alert = True     #是否继续接受下一个警告
        #初始化数据文件对象
        self.xlseng = ExcelRW.XlsEngine('E:\\Code\\yzhselenium\\test_163mail\\data\\test1.xls')
        self.xlseng.open()
    
    def test_163mail_login_logout(self):
        u'''正常登陆和退出'''
        username = self.xlseng.readcell('sheet1',2,2)
        password = self.xlseng.readcell('sheet1',2,3)
        exp_info_login = self.xlseng.readcell('sheet1',2,4)
        exp_info_logout = self.xlseng.readcell('sheet1',2,5)
        
        driver = self.driver
        login.login(driver,self.base_url,username,password)
        self.assertEqual(exp_info_login, driver.find_element_by_id("spnUid").text)
        
        login.logout(driver)
        self.assertEqual(exp_info_logout, driver.find_element_by_css_selector("h1").text)
    
    def test_163mail_login_fail(self):
        u'''非正常登陆'''
        username_list = self.xlseng.readcol('sheet1',2)
        password_list = self.xlseng.readcol('sheet1',3)
        exp_info_list = self.xlseng.readcol('sheet1',4)
        
        nrow = self.xlseng.info()[0]
        i = 2
        while i < nrow:
            driver = self.driver
            login.login(driver,self.base_url,username_list[i], password_list[i])
            self.assertEqual(exp_info_list[i], driver.find_element_by_css_selector(".error-tt>p").text)
            i = i+1
     
    def ytest_163mail_login_02(self):
        u'''不输邮箱账号和密码进行登陆'''
        driver = self.driver
        login.login(driver,self.base_url,'','')
        self.assertEqual(u"请先输入您的邮箱帐号", driver.find_element_by_css_selector(".error-tt>p").text)
        
    def ytest_163mail_login_03(self):
        u'''不输邮箱密码进行登陆'''
        driver = self.driver
        login.login(driver, self.base_url, 'defias_test', '')
        self.assertEqual(u'请输入您的密码', driver.find_element_by_css_selector(".error-tt>p").text)
        
    def ytest_163mail_login_04(self):
        u'''不输邮箱账号进行登陆'''
        driver = self.driver
        login.login(driver, self.base_url, '', 'testing')
        self.assertEqual(u'请先输入您的邮箱帐号', driver.find_element_by_css_selector('.error-tt>p').text)
        
    def ytest_163mail_login_05(self):
        u'''输入错误的邮箱账号进行登陆'''
        driver = self.driver
        login.login(driver, self.base_url, 'erroruser', 'errorpasswd')
        self.assertEqual(u'帐号或密码错误', driver.find_element_by_css_selector('.error-tt>p').text)
            
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
        
if __name__ == '__main__':
    test_suit = unittest.TestSuite()
    unittest.TextTestRunner().run(test_suit)
     
