#coding=utf8
from numpy import *

#当输出一个数组时，NumPy以特定的布局用类似嵌套列表的形式显示

a = arange(6)                          # 1d array
print a

b = arange(12).reshape(4,3)           # 2d array
print b

c = arange(24).reshape(2,3,4)         # 3d array
print c


print arange(10000)   #如果一个数组太长，则NumPy自动省略中间部分而只打印两端的数据
#可通过设置printoptions参数来禁用NumPy的这种行为并强制打印整个数组  set_printoptions(threshold='nan')
