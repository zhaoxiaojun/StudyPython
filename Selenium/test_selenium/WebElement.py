#coding=utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#获得输入框的尺寸
size=driver.find_element_by_id('kw').size
print size

#返回百度页面底部备案信息
text=driver.find_element_by_id("cp").text
print text

#返回元素的属性值，可以是 id、 name、 type 或元素拥有的其它任意属性
attribute=driver.find_element_by_id("kw").get_attribute('type')
print attribute

#返回元素的结果是否可见，返回结果为 True 或 False
result=driver.find_element_by_id("kw").is_displayed()
print result
driver.quit()