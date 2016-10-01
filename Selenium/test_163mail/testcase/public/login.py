#coding=utf-8
def login(driver,url,username,password):
    driver.get(url)
    driver.find_element_by_id("idPlaceholder").click()
    driver.find_element_by_id("idInput").clear()
    driver.find_element_by_id("idInput").send_keys(username)
    driver.find_element_by_id("pwdInput").clear()
    driver.find_element_by_id("pwdInput").send_keys(password)
    driver.find_element_by_id("loginBtn").click()

def logout(driver):
    driver.find_element_by_link_text(u"退出").click()