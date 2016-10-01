#coding=utf-8
from selenium import webdriver
from public import login, common_function
from tools import ExcelRW
import unittest,time,os,sys

class TestAd(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)    #隐式等待
        self.baseurl = 'http://192.168.10.102/'
        self.verificationErrors = []
        self.accept_next_alert = True
        #初始化数据文件对象
        self.xlseng = ExcelRW.XlsEngine('E:\\Code\\yzhselenium\\test_wifiadmin\\data\\test1.xls')
        self.xlseng.open()
                
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.driver.quit()
        self.assertEqual(self.verificationErrors, [])
    
    def test_wifiadmin_ad_add(self):
        u'''添加广告'''
        #读取数据
        adname_list = self.xlseng.readcol('sheet2',2)    #广告名称
        adtype_list = self.xlseng.readcol('sheet2',3)    #广告分类
        admaster_list = self.xlseng.readcol('sheet2',4)  #所属广告主
        adwname_list = self.xlseng.readcol('sheet2',5)   #广告位名称
        #adpicturepath_list = self.xlseng.readcol('sheet2',6)  #上传文件路径
        adtip_list = self.xlseng.readcol('sheet2',7)  #提示信息
        adnetaddress_list = self.xlseng.readcol('sheet2',8)   #目标网址
        adopenmodel_list = self.xlseng.readcol('sheet2',9)   #打开模式
        addefault_list = self.xlseng.readcol('sheet2',10)   #默认广告
        addescription_list = self.xlseng.readcol('sheet2',11)  #广告描述
        adpartnername_list = self.xlseng.readcol('sheet2',12)  #商户名称
        addefaultcity_list = self.xlseng.readcol('sheet2',13)  #默认广告地区
        exception_result_list = self.xlseng.readcol('sheet2',14)  #预期结果
        
        #nrow = self.xlseng.readcol('sheet2',1)[-1] #数据总行数，不括含首行
        nrow = self.xlseng.info('sheet2')[0]   #数据总行数，包括首行
        print "nrow: %d" %nrow
        
        #webdriver驱动
        driver = self.driver
        driver.maximize_window()  #窗口最大化
            
        i = 1
        while i < nrow:
            #获取当前时间
            now = time.strftime("%Y-%m-%d %H-%M-%S")
            
            #登录百万点系统
            login.login(driver, self.baseurl, 'test', 'testing')
        
            #点击广告
            driver.find_element_by_css_selector(".ku_fix.quike").find_element_by_xpath("h1[2]").click()
        
            #点击广告&广告位
            driver.find_element_by_css_selector("h2[accessid='11']").click()
        
            #点击广告基本信息
            driver.find_element_by_css_selector("li[accessid='32']").click()
        
            #点击“+”号
            driver.find_element_by_css_selector(".add").click()
        
            #输入广告添加所需的各字段信息
            #输入广告名称
            driver.find_element_by_css_selector("#ad_name").send_keys(adname_list[i])
            
            #广告分类下拉选择
            if adtype_list[i]:
                adtype_select = {u"商户广告":1, u"商业广告":2, u"宣传广告":3, u"友情合作广告":4, u"内测广告":5, u"WIFI认证":6, u"外测广告":7, u"宏创广告":8}
                driver.find_element_by_css_selector("#ad_cate_id").click()
                menu_select = driver.find_element_by_css_selector("#ad_cate_id").find_elements_by_tag_name("option")
                nselect = adtype_select[adtype_list[i]]
                menu_select[nselect].click()
            
                if u"商户广告" == adtype_list[i]:
                    if adpartnername_list[i]:
                        #搜索商户名称
                        driver.find_element_by_name("partner_search_key").send_keys(adpartnername_list[i])
                        driver.find_element_by_css_selector("#partner_search").click()
                        if driver.find_element_by_css_selector(".partner_search_list>ul>li").is_enabled():
                            driver.find_element_by_css_selector(".partner_search_list>ul>li").click()
                        else:
                            print u"未搜索到商户"
            
            #所属广告主下拉选择
            if admaster_list[i]:
                admaster_select = {u"百米生活":1, u"都江堰":2}
                driver.find_element_by_id("source_id").click()
                menu_select = driver.find_element_by_id("source_id").find_elements_by_tag_name("option")
                nselect = admaster_select[admaster_list[i]]
                menu_select[nselect].click()

            #广告位名称下拉选择
            if adwname_list[i]:
                adwname_select = {u"如影随形":1, u"读秒广告":2}
                driver.find_element_by_id("group_id").click()
                menu_select = driver.find_element_by_id("group_id").find_elements_by_tag_name("option")
                nselect = adwname_select[adwname_list[i]]
                menu_select[nselect].click()
            
                #文件上传
                driver.find_element_by_id("ad_up_file").click()
                #调用autoit脚本
                os.system(r"E:\Code\yzhselenium\test_wifiadmin\testcase\tools\upfile.exe")
            
            #输入提示信息
            driver.find_element_by_id("ad_tips").send_keys(adtip_list[i])
            
            #输入目标网址
            driver.find_element_by_id("ad_link").send_keys(adnetaddress_list[i])
            
            #选择打开模式
            adopenmodel_select = {u"新窗口打开":0, u"本窗口打开":1}
            radio_select = driver.find_elements_by_name("ad_open_mode")
            nselect = adopenmodel_select[adopenmodel_list[i]]
            radio_select[nselect].click()
            
            #选择默认广告
            addefault_select = {u"否":0, u"是":1}
            radio_select = driver.find_elements_by_name("is_default")
            addefault_nselect = addefault_select[addefault_list[i]]
            radio_select[addefault_nselect].click()
            #选择默认广告地区
            if 1 == addefault_nselect:
                city_list = {u"全国":0, u"北京":1, u"天津":2, u"河北":3, u"山西":4, u"内蒙古":5, u"辽宁":6, u"吉林":7, u"黑龙江":8, u"上海":9, u"江苏":10, 
                             u"浙江":11, u"安徽":12, u"福建":13, u"江西":14, u"山东":15, u"河南":16, u"湖北":17, u"湖南":18, u"广东":19, u"广西":20, 
                             u"海南":21, u"重庆":22, u"四川":23, u"贵州":24, u"云南":25, u"西藏":26, u"陕西":27, u"甘肃":28, u"青海":29, u"宁夏":30, 
                             u"新疆":31, u"台湾":32, u"香港":33, u"澳门":34}
                menu_select = driver.find_element_by_name("sc_id[]").find_elements_by_tag_name("option")
                nselect = city_list[addefaultcity_list[i]]
                menu_select[nselect].click()
            
            #输入广告描述
            driver.find_element_by_id("ad_desc").send_keys(addescription_list[i])
            
            try:
                #点击保存按钮
                driver.find_element_by_css_selector(".fsub>button").click()
                
                #接收弹窗
                if 1 == addefault_nselect:
                    driver.switch_to_alert().accept()
                
                #断言
                time.sleep(2)
                self.assertEqual(exception_result_list[i], driver.find_element_by_css_selector(".ajax_build_tip").text)  
            except Exception as e:
                print "Exception:[%s][%s]" % (sys.exc_info()[2].tb_lineno, str(e))
                screenshot_path = "E:\\Code\\yzhselenium\\test_wifiadmin\\report\\test_ad_add_errorimg" + now + ".jpg" #错误截图存放路径
                driver.get_screenshot_as_file(screenshot_path)   #错误截屏
                
            finally:
                if common_function.isElementPresent(driver, ".close"):
                    driver.find_element_by_css_selector(".close").click()
                    
                #print u"退前"    
                time.sleep(1)
                #退出百万点系统
                login.logout(driver)
                #print u"退后" 
                #time.sleep(2)
                
            #循环变量自增
            i = i+1
            #print "i is %d" % i
    
    def test_wifiadmin_ad_del(self):
        u'''删除广告'''
        #获取当前时间
        now = time.strftime("%Y-%m-%d %H-%M-%S")
            
        #webdriver驱动
        driver = self.driver
        driver.maximize_window()  #窗口最大化
        
        #登录百万点系统
        login.login(driver, self.baseurl, 'test', 'testing')
        
        #点击广告
        driver.find_element_by_css_selector(".ku_fix.quike").find_element_by_xpath("h1[2]").click()
        
        #点击广告&广告位
        driver.find_element_by_css_selector("h2[accessid='11']").click()
        
        #点击广告基本信息
        driver.find_element_by_css_selector("li[accessid='32']").click()
        
        try:
            #删除一条广告
            ad_driver_list = driver.find_elements_by_css_selector(".b_table>tbody>tr")
            ad_driver_list[4].find_element_by_css_selector("button[class='more']").click()
            ad_driver_list[4].find_element_by_css_selector("dl[class='maction']").click()
            driver.switch_to_alert().accept()
        
            self.assertEqual(u"删除成功！", driver.find_element_by_css_selector(".ajax_build_tip").text)
        except Exception as e:
            print "Exception:[%s][%s]" % (sys.exc_info()[2].tb_lineno, str(e))
            screenshot_path = "E:\\Code\\yzhselenium\\test_wifiadmin\\report\\test_ad_del_errorimg" + now + ".jpg" #错误截图存放路径
            driver.get_screenshot_as_file(screenshot_path)   #错误截屏
        finally:     
            #退出百万点系统
            time.sleep(1)
            login.logout(driver)    
    
    
    def test_wifiadmin_ad_chk(self):
        u'''成功审核广告'''
        #获取当前时间
        now = time.strftime("%Y-%m-%d %H-%M-%S")
        
        #webdriver驱动
        driver = self.driver
        driver.maximize_window()  #窗口最大化
        
        #登录百万点系统
        login.login(driver, self.baseurl, 'test', 'testing')
        
        #点击广告
        driver.find_element_by_css_selector(".ku_fix.quike").find_element_by_xpath("h1[2]").click()
        
        #点击广告&广告位
        driver.find_element_by_css_selector("h2[accessid='11']").click()
        
        #点击广告审核
        driver.find_element_by_css_selector("li[accessid='33']").click()
        
        try:
            #审核通过一条广告，点击审核按钮
            ad_driver_list = driver.find_elements_by_css_selector(".b_table>tbody>tr")
            ad_driver_list[4].find_element_by_css_selector("button[class='one']").click()

            #选择审核通过
            time.sleep(1)
            driver.find_elements_by_css_selector("input[name='audit_status']")[0].click()
            
            #输入审核说明
            driver.find_element_by_css_selector("#audit_desc").send_keys(u"测试testing")
        
            #点击提交按钮
            driver.find_element_by_css_selector("#ad_audit_btn").click()
        
            self.assertEqual(u"广告审核成功！", driver.find_element_by_css_selector(".ajax_build_tip.success").text)
        except Exception as e:
            print "Exception:[%s][%s]" % (sys.exc_info()[2].tb_lineno, str(e))
            screenshot_path = "E:\\Code\\yzhselenium\\test_wifiadmin\\report\\test_ad_chk_errorimg" + now + ".jpg" #错误截图存放路径
            driver.get_screenshot_as_file(screenshot_path)   #错误截屏
            
        finally:     
            #退出百万点系统
            time.sleep(1)
            login.logout(driver)   
            
    def test_wifiadmin_ad_modify(self):
        u'''修改广告'''
        #获取当前时间
        now = time.strftime("%Y-%m-%d %H-%M-%S")
        chuo_now = time.time()
            
        #webdriver驱动
        driver = self.driver
        driver.maximize_window()  #窗口最大化
        
        #登录百万点系统
        login.login(driver, self.baseurl, 'test', 'testing')
        
        #点击广告
        driver.find_element_by_css_selector(".ku_fix.quike").find_element_by_xpath("h1[2]").click()
        
        #点击广告&广告位
        driver.find_element_by_css_selector("h2[accessid='11']").click()
        
        #点击广告基本信息
        driver.find_element_by_css_selector("li[accessid='32']").click()
        
        #修改一条广告
        ad_driver_list = driver.find_elements_by_css_selector(".b_table>tbody>tr")
        ad_driver_list[4].find_element_by_css_selector("button[onclick]").click()
        
        #输入广告名称
        ad_name_dr = driver.find_element_by_css_selector("#ad_name")
        ad_name_new = "testadname" + str(chuo_now)
        ad_name_dr.clear()
        ad_name_dr.send_keys(ad_name_new)
    
        #输入广告分类
        driver.find_element_by_css_selector("#ad_cate_id").click()
        driver.find_element_by_css_selector("#ad_cate_id").find_elements_by_tag_name("option")[7].click()
        
        #输入所属广告主
        driver.find_element_by_id("source_id").click()
        driver.find_element_by_id("source_id").find_elements_by_tag_name("option")[2].click()
        
        #文件上传
        driver.find_element_by_id("ad_up_file").click()
        os.system(r"E:\Code\yzhselenium\test_wifiadmin\testcase\tools\upfile.exe") 

        #输入目标网址
        driver.find_element_by_id("ad_link").send_keys("http://m.100msh.com")  
        
        #输入广告描述
        driver.find_element_by_id("ad_desc").send_keys("test ad modiy discription")
         
        try:
            #点击保存按钮
            driver.find_element_by_css_selector(".fsub>button").click()
        
            self.assertEqual(u"广告修改成功！", driver.find_element_by_css_selector(".ajax_build_tip").text)
        except Exception as e:
            print "Exception:[%s][%s]" % (sys.exc_info()[2].tb_lineno, str(e))
            screenshot_path = "E:\\Code\\yzhselenium\\test_wifiadmin\\report\\test_ad_modify_errorimg" + now + ".jpg" #错误截图存放路径
            driver.get_screenshot_as_file(screenshot_path)   #错误截屏
        finally:     
            #退出百万点系统
            time.sleep(1)
            login.logout(driver)
        
if __name__ == '__main__':
    unittest.main()
    
    