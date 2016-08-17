#encoding: utf-8

import testa   #第一次会打印a里面的语句
import os  #再次导入os后，其内存地址和a里面的是一样的，因此这里只是对os的本地引用
print 'in c',id(os)
import testa  #第二次不会打印a里面的语句，因为没有重新加载


#结论：多次重复使用import语句时，不会重新加载被指定的模块，只是把对该模块的内存地址给引用到本地变量环境
