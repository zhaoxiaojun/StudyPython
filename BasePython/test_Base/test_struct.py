#coding=utf8
import struct
"""
struct模块中最重要的三个函数是pack(), unpack(), calcsize()
pack(fmt, v1, v2, ...)     按照给定的格式(fmt)，把数据封装成字符串(实际上是类似于c结构体的字节流)
unpack(fmt, string)       按照给定的格式(fmt)解析字节流string，返回解析出来的tuple
calcsize(fmt)                 计算给定的格式(fmt)占用多少字节的内存

Format      C Type          Python                  字节数
-----------------------------------------------------------
x           pad byte        no value                1
c           char            string of length 1      1
b           signed char     integer                 1
B           unsigned char   integer                 1
?           _Bool           bool                    1
h           short           integer                 2
H           unsigned short  integer                 2
i           int             integer                 4
I           unsigned int    integer or long         4
l           long            integer                 4
L           unsigned long   long                    4
q           long long       long                    8
Q           unsigned long long  long                8
f           float           float                   4
d           double          float                   8
s           char[]          string                  1
p           char[]          string                  1
P           void *          long

考虑字节对齐 前缀：
Character   Byte order              Size and alignment
--------------------------------------------------------
@           native                  native  凑够4个字节
=           native                  standard    按原字节数
<           little-endian           standard    按原字节数
>           big-endian              standard    按原字节数
!           network(= big-endian)   standard    按原字节数
"""

'''
pack的第一个参数是处理指令，'>I'的意思是：表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
后面的参数个数要和处理指令一致。
'''
print struct.pack('>I', 10240099)   #把任意数据类型变成bytes

#print struct.pack('>II', 10240099, 10240099)   #多参数

'''
根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数
'''
print struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')   #把bytes变成相应的数据类型


#分析windows的位图文件.bmp（一种非常简单的文件格式）
bmp_header = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print struct.unpack('<ccIIIIIIHH', bmp_header)
