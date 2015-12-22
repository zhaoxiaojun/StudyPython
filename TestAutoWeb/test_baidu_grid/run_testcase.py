#coding=utf-8
import unittest,time,os
import HTMLTestRunner
import multiprocessing

#测试用例存放目录
test_dir = "E:\\Code\\yzhselenium\\test_baidu_grid\\testcase\\"

test_suit_list = []   #测试套组
for test_dirtd in os.listdir(test_dir):
    if 'testcase' in test_dirtd:
        test_dirn = test_dir+test_dirtd
        #自动发现测试用例并生成测试套组
        test_suit_list.append(unittest.defaultTestLoader.discover(test_dirn, pattern='test*.py', top_level_dir=test_dirn))
         

def MprocessRunCase(test_lists):
    #进程组
    process_list = []
    
    #获取当前时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")
        
    #测试报告存放路径
    report_path = r"E:\Code\yzhselenium\test_baidu_grid\report\result" + now + ".html"
        
    #测试报告文件句柄
    fp = file(report_path, 'wb')
        
    #装载进程组
    for i in test_lists:
        report_runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：' )
        proc = multiprocessing.Process(target= report_runner.run(i),args=(i,))
        process_list.append(proc)
    
    #启动进程
    for proc in process_list:
        proc.start()
    
    #守护进程
    for proc in process_list:
        proc.join()
    
    fp.close()
    

if __name__ == "__main__":
    MprocessRunCase(test_suit_list)
    
    