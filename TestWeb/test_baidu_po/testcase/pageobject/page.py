#coding=utf-8
from selenium import webdriver

class Page(object):
    u'''基本类，用于所有页面继承'''

    def __init__(self,base_browser,base_url):
        self.url = base_url              #URL
        if 'firefox' == base_browser:
            self.driver = webdriver.Firefox()    #驱动
        elif 'chrome' == base_browser:
            self.driver = webdriver.Chrome()
        else:
            print "init error!"
            return -1
        
    def open_url(self):                #打开URL地址
        self.driver.get(self.url)
    
    def find_emt(self,loc_type,loc_value):      #元素定位
        return self.driver.find_element(loc_type,loc_value)
    
    def run_js(self):                  #执行js脚本
        return self.driver.execute_script()

    def close_browser(self,):
        self.driver.close()