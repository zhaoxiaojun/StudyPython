#coding=utf-8
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

#判断元素是否存在
def isElementPresent(driver, selector):
    try:
        driver.find_element(By.CSS_SELECTOR,selector)
        return True
    except NoSuchElementException:
        return False