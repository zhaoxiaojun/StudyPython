#coding=utf-8
from selenium.webdriver.common.by import By
from time import sleep
from page import Page

class BaiduPage(Page):
    u'''百度搜索首页'''
    
    def open_baidu(self):               #打开百度搜索页面
        self.open_url(self.url)
    
    def input_search(self,str_search):   #输入搜索字符
        self.find_emt(By.ID, "kw").send_keys(str_search)
        
    def click_searchbutton(self):       #点击搜索按钮
        self.find_emt(By.ID, "su").click()
        sleep(1)
        