#coding=utf8
import struct

'''
pack的第一个参数是处理指令，'>I'的意思是：表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
后面的参数个数要和处理指令一致。
'''
print struct.pack('>I', 10240099)   #把任意数据类型变成bytes


'''
根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数
'''
print struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')   #把bytes变成相应的数据类型


#分析windows的位图文件.bmp（一种非常简单的文件格式）
bmp_header = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print struct.unpack('<ccIIIIIIHH', bmp_header)
