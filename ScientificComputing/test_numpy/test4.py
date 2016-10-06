#coding=utf8
import numpy as np
from numpy import *

#数组索引，切片，赋值
a = array( [[2,3,4],[5,6,7]] )
print a

print a[1,2]

print a[1,:]

a[1,:] = [8,9,10]
print a
print ''

#数组的加减乘除
a = ones((2,2))
b = eye(2)
print a
print b
print ''

print a > 2

print a+b

print a-b

print b*2

print (a*2)*(b*2)

print b/(a*2)

print (a*2)**4
print ''

#数组对象自带的方法
print a.sum()

print  a.sum(axis=0)  #计算每一列（二维数组中类似于矩阵的列）的和

print a.min()

print a.max()
print ''


#使用numpy的方法
print np.sin(a)

print np.max(a)

print np.floor(a)

print np.exp(a)

print np.dot(a,a)  #矩阵乘法
print ''

#合并数组
a = np.ones((2,2))
b = np.eye(2)
c = np.hstack((a,b))
d = np.vstack((a,b))

print d
print c

a[1,1] = 5
b[1,1] = 5
print c  #a、b中元素的改变并未影响c




#深拷贝数组
a = np.ones((2,2))
b = a
print b is a

c = a.copy()
print c is a



