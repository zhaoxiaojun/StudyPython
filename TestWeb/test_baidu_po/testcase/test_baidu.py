#coding=utf-8
from selenium import webdriver
from pageobject import baidupage

test_baidupage = baidupage.BaiduPage('firefox','http://www.baidu.com')

#访问url
test_baidupage.open_url()

#搜索框输入
test_baidupage.input_search("selenium2")

#点击搜索按钮
test_baidupage.click_searchbutton()


#关闭浏览器
test_baidupage.close_browser()