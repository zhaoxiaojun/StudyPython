#coding=utf-8
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    #desired_capabilities=DesiredCapabilities.CHROME
    desired_capabilities={
                    'platform':'ANY',
                    'browserName':'chrome',
                    'version':'',
                    'javascriptEnabled':True
                }
                
    )
driver.get('http://www.baidu.com')
driver.quit()