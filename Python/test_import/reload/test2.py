#encoding: utf-8


import sys
reload(sys)
sys.setdefaultencoding('utf8')
del sys.setdefaultencoding   ##删除原来的setdefaultencoding函数
sys.setdefaultencoding('gb2312') #报错



"""
那么到底是谁在之前就导入sys并且调用了setdefaultencoding函数呢？
答案就在python安装目录的Lib文件夹下，有一个叫site.py的文件【python2.6】，在里面可以找到main() --> setencoding()-->
sys.setdefaultencoding(encoding),因为这个site.py每次启动python解释器时会自动加载，所以main函数每次都会被执行，
setdefaultencoding函数一出来就已经被删除了
"""
