#coding=utf-8
from selenium import webdriver
import os

#设置firefox的about:config
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList",2) #设置成0代表下载到浏览器默认下载路径；设置成2则可以保存到指定目录
fp.set_preference("browser.download.manager.showWhenStarting",False)   #设置成 0 代表下载到浏览器默认下载路径；设置成 2 则可以保存到指定目录
fp.set_preference("browser.download.dir", os.getcwd()) #用于指定你所下载文件的目录。 os.getcwd() 该函数不需要传递参数，用于返回当前的目录
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream") #下载文件的类型

driver = webdriver.Firefox(firefox_profile=fp)
driver.get("http://pypi.Python.org/pypi/selenium")
driver.find_element_by_partial_link_text("selenium-2").click()