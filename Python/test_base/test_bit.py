#coding=utf8

#位运算

#按位与运算&， 按位与是指一个数字转化为二进制，然后这些二进制的数按位来进行与运算
operationNumber = 7 & 18
print operationNumber   #2


#按位或运算|， 按位或是指一个数字转化为二进制，然后这些二进制的数按位来进行或运算
operationNumber = 7 | 18
print operationNumber        #23

#按位异或
operationNumber = 7 ^ 18
print operationNumber        #21

#按位翻转 ~   按位翻转公式: ~x = - (x+1)
operationNumber = ~12   #~12=- (12+1) = -13
print operationNumber

#左移<<
'''
比如18左移就是将他的二进制形式00100100左移，得到00100100(36)
左移规律:左移一个单位相当于乘2，左移两个单位相当于乘以4，左移三个单位相当于乘以8，
即: 左移n个单位相当于乘以2的n次幂
'''
operationNumber = 12 << 1
print operationNumber        #24

operationNumber = 3 << 3
print operationNumber        #24


#右移>>
'''
理解左移以后，右移就很好理解了。
右移是左移的逆运算，将对应的二进制数向右移动
右移规律:右移一个单位相当于除以2，右移两个单位相当于除以4，右移三个单位相当于除以8
即: 右移n个单位相当于除以2的n次幂
'''
operationNumber = 12 >> 1
print operationNumber        #6

operationNumber = 12 >> 2
print operationNumber        #3




