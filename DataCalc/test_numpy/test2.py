#coding=utf8
import numpy as np

#数据类型转换
print np.float64(42)
print np.int8(42.0)
print np.bool(42)
print np.bool(42.0)
print np.float(True)


#创建一个全是0的数组
a = np.zeros((3,4))
print a
print a.dtype  #默认创建的数组类型(dtype)都是float64
print a.itemsize  #每个元素所占的字节数
print a.ndim  #数组的维数
print a.shape  #数组每一维的大小
print a.size   #数组的元素数


#创建一个全为1的数组
b = np.ones((2,3,4), dtype=np.int16)  #手动指定数组中元素类型
print b

#创建一个xxx数组
print np.eye(4)

#创建一个内容随机并且依赖与内存状态的数组
c = np.empty((2,3))
print c


#返回一个数列形式的数组
print np.arange(10, 30, 5)  #以10开始，差值为5的等差数列

print np.arange(15)  #以0开始，差值为1的等差数列

print np.arange(0,2,0.5)  #当arange使用浮点数参数时，由于浮点数精度有限，通常无法预测获得的元素个数

print np.linspace(1,3,9)  #从1到3中产生9个数

