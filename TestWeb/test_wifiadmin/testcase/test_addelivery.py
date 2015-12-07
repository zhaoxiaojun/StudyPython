#coding=utf-8
from selenium import webdriver
from public import login, common_function
from tools import ExcelRW
import unittest,time,sys

class TestAddelivery(unittest.TestCase):
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
    
    def test_wifiadmin_addelivery_add(self):
        u'''添加广告投放'''
        #读取数据
        addelivery_name_list = self.xlseng.readcol('sheet3',2)    #广告投放名称
        deliveryad_name_list = self.xlseng.readcol('sheet3',3)    #投放广告名称
        addelivery_type_list = self.xlseng.readcol('sheet3',4)  #投放类型
        delivery_date_list = self.xlseng.readcol('sheet3',5)   #投放日期段
        delivery_time_list = self.xlseng.readcol('sheet3',6)  #投放时间段
        addelivery_model_list = self.xlseng.readcol('sheet3',7)  #投放参数
        addelivery_address_list = self.xlseng.readcol('sheet3',8)   #投放地区
        partner_type_list = self.xlseng.readcol('sheet3',9)   #商户分类
        partner_tip_list = self.xlseng.readcol('sheet3',10)   #商户标签
        delivery_partner_list = self.xlseng.readcol('sheet3',11)   #投放商户名称
        addelivery_description_list = self.xlseng.readcol('sheet3',12)  #投放说明
        exception_result_list = self.xlseng.readcol('sheet3',13)  #预期结果
        
        nrow = self.xlseng.info('sheet3')[0]   #数据总行数，包括首行
        #print "nrow: %d" %nrow
        
        i = 1
        while i < nrow:
            #获取当前时间
            now = time.strftime("%Y-%m-%d %H-%M-%S")
        
            #webdriver驱动
            driver = self.driver
            driver.maximize_window()  #窗口最大化
            
            #登录百万点系统
            login.login(driver, self.baseurl, 'test', 'testing')
        
            #点击广告
            driver.find_element_by_css_selector(".ku_fix.quike").find_element_by_xpath("h1[2]").click()
        
            #点击广告投放
            driver.find_element_by_css_selector("h2[accessid='10']").click()
        
            #点击投放管理
            driver.find_element_by_css_selector("li[accessid='27']").click()
        
            #点击“+”号
            driver.find_element_by_css_selector(".add").click()
        
            #输入广告投放添加所需的各字段信息
            #输入广告投放名称
            driver.find_element_by_css_selector("input[name='delivery_name']").send_keys(addelivery_name_list[i])
        
            #输入投放广告名称
            if deliveryad_name_list[i]:
                driver.find_element_by_css_selector("input[name='ad_search_key']").send_keys(deliveryad_name_list[i])
                driver.find_element_by_css_selector("button#ad_search").click()
                driver.find_element_by_css_selector(".ad_search_list>ul>li").click()
        
            #输入投放类型
            if addelivery_type_list[i]:
                addelivery_type_select = {u"定时广告":1, u"推送广告":2}
                driver.find_element_by_name("ad_type_id").click()
                menu_select = driver.find_element_by_name("ad_type_id").find_elements_by_tag_name("option")
                nselect = addelivery_type_select[addelivery_type_list[i]]
                menu_select[nselect].click()
        
            #输入投放日期段
            delivery_date_startend = delivery_date_list[i].split('|')
            delivery_start_date = delivery_date_startend[0]
            delivery_end_date = delivery_date_startend[1]
            driver.find_element_by_css_selector("input[name='delivery_start_date']").send_keys(delivery_start_date)
            driver.find_element_by_css_selector("input[name='delivery_end_date']").send_keys(delivery_end_date)
        
            #输入投放时间段
            delivery_time_startend = delivery_time_list[i].split('|')
            delivery_start_time = delivery_time_startend[0]
            delivery_end_time = delivery_time_startend[1]
            driver.find_element_by_css_selector("input[name='delivery_start_time']").send_keys(delivery_start_time)
            driver.find_element_by_css_selector("input[name='delivery_end_time']").send_keys(delivery_end_time)
        
            #输入投放参数
            addelivery_model_select = {u"综合投放":0, u"商户投放":1}
            radio_select = driver.find_elements_by_name("delivery_parm")
            addelivery_model_nselect = addelivery_model_select[addelivery_model_list[i]]
            radio_select[addelivery_model_nselect].click()
        
            if u'商户投放' == addelivery_model_list[i]:
                #输入商户
                if delivery_partner_list[i]:
                    driver.find_element_by_css_selector("input[name='partner_search_key']").send_keys(delivery_partner_list[i])
                    driver.find_element_by_css_selector("button#partner_search").click()
                    driver.find_element_by_css_selector("div.partner_search_list>ul>li").click()
        
            elif u'综合投放' == addelivery_model_list[i]:
                #输入投放地区
                addelivery_address_province = {u"全国":0, u"北京":11, u"天津":12, u"河北":13, u"山西":14, u"内蒙古":15, u"辽宁":21, u"吉林":22, u"黑龙江":23, 
                                       u"上海":31, u"江苏":32, u"浙江":33, u"安徽":34, u"福建":35, u"江西":36, u"山东":37, u"河南":41, u"湖北":42, u"湖南":43, 
                                       u"广东":44, u"广西":45, u"海南":46, u"重庆":50, u"四川":51, u"贵州":52, u"云南":53, u"西藏":54, u"陕西":61, u"甘肃":62, 
                                       u"青海":63, u"宁夏":64, u"新疆":65, u"台湾":71, u"香港":81, u"澳门":91}
                
                addelivery_address_city = {u"深圳":4403, u"广州":4401, u"韶关":4402, u"珠海":4404, u"汕头":4405, u"佛山":4406, u"江门":4406, u"湛江":4408, 
                                           u"茂名":4409, u"肇庆":4412, u"惠州":4413, u"梅州":4414, u"汕尾":4415, u"河源":4416, u"阳江":4417, u"清远":4418, 
                                           u"东莞":4419, u"中山":4420, u"潮州":4421, u"揭阳":4452, u"云浮":4453}
                
                addelivery_address_area = {u"罗湖区":440303, u"福田区":440304, u"南山区":440305, u"宝安区":440306, u"龙岗区":440307, u"盐田区":440308, 
                                           u"坪山新区":910163, u"龙华新区":910165, u"大鹏新区":910166, u"市辖区":440101, u"荔湾区":440103, u"越秀区":440104, 
                                           u"海珠区":440105, u"天河区":440106, u"白云区":440111, u"黄埔区":440112, u"番禺区":440113, u"花都区":440114, 
                                           u"增城区":440183, u"从化区":440184}
                
                addelivery_address_cirle = {u"东门":101, u"地王大厦":102, u"国贸":103, u"黄贝岭":104, u"火车站":105, u"万象城":109, u"莲塘":106, u"笋岗":107, 
                                            u"CBD中心区":82, u"车公庙":83, u"福田保税区":84, u"岗厦":85, u"华强北":86, u"皇岗":87, u"华强南":88, u"景田":89, 
                                            u"梅林":90, u"市民中心":92, u"香蜜湖":95, u"竹子林":96, u"科学城":1042, u"开发区东区":1043, u"开发区西区":1044, 
                                            u"中心城":1045, u"其他（广州）":1080}
                
                if addelivery_address_list[i]:
                    addelivery_address = addelivery_address_list[i].split('|')
                    naddress = len(addelivery_address)
                    if 0 < naddress:
                        #输入省份
                        driver.find_element_by_css_selector("select[name='sc_id[]']").click()
                        nprovince = addelivery_address_province[addelivery_address[0]]
                        elestr_nprovince = "option[value='" + str(nprovince) + "']"
                        driver.find_element_by_css_selector("select[name='sc_id[]']").find_element_by_css_selector(elestr_nprovince).click()
                        if 1 < naddress:
                            #输入城市
                            time.sleep(1)
                            driver.find_elements_by_css_selector("select[name='sc_id[]']")[1].click()
                            ncity = addelivery_address_city[addelivery_address[1]]
                            elestr_ncity = "option[value='" + str(ncity) + "']"
                            driver.find_elements_by_css_selector("select[name='sc_id[]']")[1].find_element_by_css_selector(elestr_ncity).click()
                            if 2 < naddress:
                                #输入区
                                time.sleep(1)
                                driver.find_elements_by_css_selector("select[name='sc_id[]']")[2].click()
                                narea = addelivery_address_area[addelivery_address[2]]
                                elestr_narea = "option[value='" + str(narea) + "']"
                                driver.find_elements_by_css_selector("select[name='sc_id[]']")[2].find_element_by_css_selector(elestr_narea).click()
                                if 3 < naddress:
                                    #输入商圈
                                    driver.find_element_by_css_selector("select[name='area_id[]']").click()
                                    ncirle = addelivery_address_cirle[addelivery_address[3]]
                                    elestr_ncirle = "option[value='" + str(ncirle) + "']"
                                    driver.find_element_by_css_selector("select[name='area_id[]']").find_element_by_css_selector(elestr_ncirle).click()
                    #点击添加按钮
                    driver.find_element_by_css_selector("button#add_area").click()
                                     
                #输入商户分类
                partner_type1 = {u"全部":0, u"餐饮美食":1, u"娱乐休闲":2, u"都市丽人":37, u"婚嫁服务":39, u"购物零售":40, u"家庭亲子":41, u"运动健身":74, 
                                 u"酒店住宿":89, u"汽车服务":90, u"生活服务":91, u"公共交通":229}

                partner_type2 = {u"北京菜":92, u"火锅":93, u"日本菜":94, u"西餐":95, u"自助餐":96, u"面包甜点":97, u"韩国料理":98, u"川菜":99, u"鲁菜":100, 
                                 u"湘菜":101, u"湖北菜":102, u"江浙菜":103, u"粤菜":104, u"东北菜":105, u"清真菜":106, u"新疆菜":107, u"西北菜":108, 
                                 u"云南菜":109, u"贵州菜":110, u"素菜":111, u"海鲜":112, u"小吃快餐":113, u"东南亚菜":114, u"其他":115, u"烧烤":221, 
                                 u"茶饮":226, u"茶餐厅":227, u"微菜":236}
                
                if partner_type_list[i]:
                    partner_type = partner_type_list[i].split('|')
                    npartner_type = len(partner_type)
                    if 0 < npartner_type:
                        driver.find_element_by_css_selector("select[name='cat_id[]']").click()
                        npartner_type1 = partner_type1[partner_type[0]]
                        elestr_type1 = "option[value='" + str(npartner_type1) + "']"
                        driver.find_element_by_css_selector("select[name='cat_id[]']").find_element_by_css_selector(elestr_type1).click()
                        if 1 < npartner_type:
                            time.sleep(1)
                            driver.find_elements_by_css_selector("select[name='cat_id[]']")[1].click()
                            npartner_type2 = partner_type2[partner_type[1]]
                            elestr_type2 = "option[value='" + str(npartner_type2) + "']"
                            driver.find_elements_by_css_selector("select[name='cat_id[]']")[1].find_element_by_css_selector(elestr_type2).click()
                    
                    #点击添加按钮
                    driver.find_element_by_css_selector("button#add_cate").click()
                
                #输入商户标签
                partner_tip = {u"全部":0, u"商务":7, u"养生":8, u"送礼":9, u"电影":10, u"聚餐":11, u"宴请":12, u"约会":13}
                if partner_tip_list[i]:
                    npartner_tip = partner_tip[partner_tip_list[i]]
                    elestr_tip = "option[value='" + str(npartner_tip) + "']"
                    driver.find_element_by_css_selector("select[name='tag_id[]']").find_element_by_css_selector(elestr_tip).click()
                                    
                    #点击添加按钮
                    driver.find_element_by_css_selector("button#add_tag").click()
            else:
                print "addelivery_model is error!"
            
            #输入投放说明
            driver.find_element_by_css_selector("textarea[name='delivery_desc']").send_keys(addelivery_description_list[i])
               
            try:
                #点击保存按钮
                driver.find_element_by_css_selector(".fsub>button").click()
                
                #断言
                time.sleep(2)
                self.assertEqual(exception_result_list[i], driver.find_element_by_css_selector(".ajax_build_tip").text)  
            
            except Exception as e:
                print "Exception:[%s][%s]" % (sys.exc_info()[2].tb_lineno, str(e))
                screenshot_path = "E:\\Code\\yzhselenium\\test_wifiadmin\\report\\test_addelivery_add_errorimg" + now + ".jpg" #错误截图存放路径
                driver.get_screenshot_as_file(screenshot_path)   #错误截屏

            finally:
                if common_function.isElementPresent(driver, ".close"):
                    driver.find_element_by_css_selector(".close").click()
                    
                #退出百万点系统
                time.sleep(1)
                login.logout(driver)

            #循环变量自增
            i = i+1
            
    
    def test_wifiadmin_addelivery_del(self):
        u"删除广告投放"
        #获取当前时间
        now = time.strftime("%Y-%m-%d %H-%M-%S")
            
        #webdriver驱动
        driver = self.driver
        driver.maximize_window()  #窗口最大化
        
        #登录百万点系统
        login.login(driver, self.baseurl, 'test', 'testing')
        
        #点击广告
        driver.find_element_by_css_selector(".ku_fix.quike").find_element_by_xpath("h1[2]").click()
        
        #点击广告投放
        driver.find_element_by_css_selector("h2[accessid='10']").click()
        
        #点击投放管理
        driver.find_element_by_css_selector("li[accessid='27']").click()
        
        try:
            #勾选一条广告投放  默认第一条被勾选
            #addelivery_driver_list = driver.find_elements_by_css_selector(".b_table>tbody>tr")
            #addelivery_driver_list[0].find_element_by_css_selector(".checkbox").click()
     
            #点击删除按钮
            driver.find_element_by_css_selector(".del").click()
            
            #弹窗确定
            driver.switch_to_alert().accept()
        
            self.assertEqual(u"投放广告删除成功!", driver.find_element_by_css_selector(".ajax_build_tip").text)
        
        except Exception as e:
            print "Exception:[%s][%s]" % (sys.exc_info()[2].tb_lineno, str(e))
            screenshot_path = "E:\\Code\\yzhselenium\\test_wifiadmin\\report\\test_addelivery_del_errorimg" + now + ".jpg" #错误截图存放路径
            driver.get_screenshot_as_file(screenshot_path)   #错误截屏
        
        finally:     
            #退出百万点系统
            time.sleep(1)
            login.logout(driver)   
               
    
    def test_wifiadmin_addelivery_chk(self):
        u"审核广告投放"
        #获取当前时间
        now = time.strftime("%Y-%m-%d %H-%M-%S")
        
        #webdriver驱动
        driver = self.driver
        driver.maximize_window()  #窗口最大化
        
        #登录百万点系统
        login.login(driver, self.baseurl, 'test', 'testing')
        
        #点击广告
        driver.find_element_by_css_selector(".ku_fix.quike").find_element_by_xpath("h1[2]").click()
        
        #点击广告投放
        driver.find_element_by_css_selector("h2[accessid='10']").click()
        
        #点击投放审核
        driver.find_element_by_css_selector("li[accessid='29']").click()
        
        try:
            #审核通过一条广告，点击审核按钮
            addelivery_driver_list = driver.find_elements_by_css_selector(".b_table>tbody>tr")
            addelivery_driver_list[0].find_element_by_css_selector("button[class='one']").click()

            #选择审核通过
            time.sleep(1)
            driver.find_elements_by_css_selector("input[name='audit_status']")[0].click()
            
            #输入审核说明
            driver.find_element_by_css_selector("#audit_remark").send_keys(u"测试testing")
        
            #点击提交按钮
            driver.find_element_by_css_selector(".fsub").find_element_by_css_selector("button[type='submit']").click()
        
            self.assertEqual(u"广告投放审核成功", driver.find_element_by_css_selector(".ajax_build_tip.success").text)
        except Exception as e:
            print "Exception:[%s][%s]" % (sys.exc_info()[2].tb_lineno, str(e))
            screenshot_path = "E:\\Code\\yzhselenium\\test_wifiadmin\\report\\test_addelivery_chk_errorimg" + now + ".jpg" #错误截图存放路径
            driver.get_screenshot_as_file(screenshot_path)   #错误截屏
            
        finally:     
            #退出百万点系统
            time.sleep(1)
            login.logout(driver)
    
if __name__ == '__main__':
    unittest.main()
    