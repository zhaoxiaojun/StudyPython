#coding=utf8
import pyh

page = pyh.PyH('My wonderful PyH page')

tab = page << pyh.table()
tab.attributes['border'] = '1'   #表格边框
tab.attributes['cellpadding'] = '1'   #单元格边沿与其内容之间的空白
tab.attributes['cellspacing'] = '0'   #单元格之间间隔
tab.attributes['cl'] = 'table'
tab.attributes['borderColor'] = '#504F4F'
tab.attributes['width'] = '90%'

tab << pyh.tr(pyh.th(u'用例ID'.encode('gbk'), bgcolor='#E6E6FA', align='left') + pyh.th(u'用例名称'.encode('gbk'), bgcolor='#E6E6FA', align='left') +
pyh.th(u'测试项'.encode('gbk'), bgcolor='#E6E6FA', align='left') + pyh.th(u'测试项类型'.encode('gbk'), bgcolor='#E6E6FA', align='left') +
pyh.th(u'测试结果'.encode('gbk'), bgcolor='#E6E6FA', align='left') + pyh.th(u'提示信息'.encode('gbk'), bgcolor='#E6E6FA', align='left'))

testcase_result = {('Sheet1',1):('PASS','PASS info'), ('Sheet1',2):('PASS','PASS info')}


testresult = testcase_result[('Sheet1', 1)][0]
            #if u'PASS' == testresult:
            #    testinfo = u'pass'
            #else:
testinfo = testcase_result[('Sheet1', 1)][1]

tab << pyh.tr(pyh.th(testresult.encode('gbk'), bgcolor='#00ff00', align='left') + pyh.th(testinfo.encode('gbk'), align='left'))


page.printOut('testing_rep.html')
page.printOut()
