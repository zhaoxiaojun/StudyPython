#coding=utf-8
from selenium import webdriver
import time

#解决chrome浏览器提示您使用的是不受支持的命令行标记问题
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

#启动chrome浏览器
chdriver = webdriver.Chrome(chrome_options=options)

#访问URL
chdriver.get('http://www.baidu.com')

time.sleep(0.3)
#搜索框输入
chdriver.find_element_by_id('kw').send_keys('chromedriver')

#点击搜索按钮
chdriver.find_element_by_id('su').click()

time.sleep(3)
#断言结果
assert(u"chromedriver_百度搜索" == chdriver.title),'Test Rusult:Fail'
print 'Test Rusult:Pass'

chdriver.close()