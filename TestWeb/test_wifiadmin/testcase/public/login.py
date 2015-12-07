#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains

def login(driver,url,username,password):
    driver.get(url)
    driver.find_element_by_class_name("name").click()
    driver.find_element_by_class_name("name").clear()
    driver.find_element_by_class_name("name").send_keys(username)
    driver.find_element_by_class_name("pwd").clear()
    driver.find_element_by_class_name("pwd").send_keys(password)
    driver.find_element_by_id("submit").click()

def logout(driver):
    menu_test = driver.find_element_by_css_selector(".user.name") 
    ActionChains(driver).move_to_element(menu_test).click(menu_test).perform()
    click_logout = driver.find_element_by_css_selector("dd[onclick=\"location.href='http://192.168.10.102/login/out'\"]")
    click_logout.click()