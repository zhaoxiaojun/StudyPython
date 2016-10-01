#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest,time
#导入公共函数文件
from public import login
from tools import ExcelRW

class TestLogin(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)     #设置整个页面的隐性等待时间
        self.base_url = "http://192.168.10.102/"
        self.verificationErrors = []      #错误信息保存数组
        self.accept_next_alert = True     #是否继续接受下一个警告
        #初始化数据文件对象
        self.xlseng = ExcelRW.XlsEngine('E:\\Code\\yzhselenium\\test_wifiadmin\\data\\test1.xls')
        self.xlseng.open()
         
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    
    def test_wifiadmin_login_logout(self):
        u'''正常登陆和退出'''
        username = self.xlseng.readcell('sheet1',2,2)
        password = self.xlseng.readcell('sheet1',2,3)
        exp_info_login = self.xlseng.readcell('sheet1',2,4)
        exp_info_logout = self.xlseng.readcell('sheet1',2,5)
        
        driver = self.driver
        login.login(driver,self.base_url,username,password)
        self.assertEqual(exp_info_login, driver.find_element_by_css_selector("div.hi>h1").text)
        
        time.sleep(2)
        login.logout(driver)
        self.assertEqual(exp_info_logout, driver.current_url)
        
    def test_wifiadmin_login_erroruser(self):
        u'''输入错误的用户名密码登陆'''
        username = self.xlseng.readcell('sheet1',3,2)
        password = self.xlseng.readcell('sheet1',3,3)
        exp_info_login = self.xlseng.readcell('sheet1',3,4)
        
        driver = self.driver
        login.login(driver,self.base_url,username,password)
        self.assertEqual(exp_info_login, driver.find_element_by_css_selector("div.msg>p").text)                
        
    
    def test_wifiadmin_login_fail(self):
        u'''非正常登陆'''
        username_list = self.xlseng.readcol('sheet1',2)
        password_list = self.xlseng.readcol('sheet1',3)
        exp_info_list = self.xlseng.readcol('sheet1',4)
         
        nrow = self.xlseng.info()[0]   #数据总行数，包括首行
        i = 3
        while i < nrow:
            driver = self.driver
            login.login(driver,self.base_url,username_list[i], password_list[i])
            self.assertEqual(exp_info_list[i], driver.find_element_by_css_selector("div.msg").text)
            i = i+1
            
if __name__ == '__main__':
    test_suit = unittest.TestSuite()
    unittest.TextTestRunner().run(test_suit)
     
     
     

