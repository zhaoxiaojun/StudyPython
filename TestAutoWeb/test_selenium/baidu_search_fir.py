#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#启动firefox浏览器
browser = webdriver.Firefox()

#访问url
browser.get("http://www.baidu.com")

#休眠0.3秒
time.sleep(0.3)

#搜索框输入
#browser.find_element_by_id("kw").send_keys("selenium2")
browser.find_element(By.ID, "kw").send_keys("selenium2")

#点击搜索按钮
#browser.find_element_by_id("su").click()
#browser.find_element(By.ID, "su").click()
browser.find_element(By.ID, "su").submit()

time.sleep(3)

#断言结果
assert(u"selenium2_百度搜索" == browser.title),'Test Rusult:Fail'
print 'Test Rusult:Pass'

#关闭浏览器
browser.close()