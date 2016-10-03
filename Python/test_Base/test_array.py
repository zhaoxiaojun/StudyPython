#coding=utf8
from array import array

"""
python的array和C的数组很类似，它只能存储同样地数据类型的数据。它所占的存储空间的大小就是数据的大小
array就是披上了python外衣的C的数组

Type code   C Type          Python Type    Minimum size in bytes
'c'         char            character       1
'b'         signed char     int             1
'B'         unsigned char   int             1
'u'         Py_UNICODE      Unicode character   2 (see note)
'h'         signed short    int 2
'H'         unsigned short  int 2
'i'         signed int      int 2
'I'         unsigned int    long    2
'l'         signed long     int 4
'L'         unsigned long   long    4
'f'         float           float   4
'd'         double          float   8
"""


#创建一个interger类型的数组
myarr = array("l")
print myarr

#追加元素
myarr.append(3)
myarr.append(1)
myarr.append(8)
myarr.append(9)
myarr.append(8)
myarr.append(8)
print myarr

#删除最后一个
myarr.pop()
print myarr

#删除数组中第一个指定的值
myarr.remove(8)
print myarr

#取数组的值 通过下标
num1 = myarr[0]   #第一个值
print myarr


#指定位置插入值　　　
myarr.insert(6,10)    #6表示下标 10表示要插入的值
print myarr


#数组反序
myarr.reverse()
print myarr


