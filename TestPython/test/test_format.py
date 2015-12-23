#coding=utf8
'''
自python2.6开始，新增了一种格式化字符串的函数str.format()，可谓威力十足
通过{}和:来代替%
'''

#通过位置
print '{0},{1}'.format('kzc',18)   #字符串的format函数可以接受不限个参数，位置可以不按顺序，可以不用或者用多次，不过2.6不能为空{}，2.7才可以
print '{},{}'.format('kzc',18)
print '{1},{0},{1}'.format('kzc',18)


#通过关键字参数
print '{name},{age}'.format(age=18,name='kzc')


#通过对象属性
class Person:
    def __init__(self,name,age):
        self.name,self.age = name,age
    def __str__(self):
        return 'This guy is {self.name},is {self.age} old'.format(self=self)

print str(Person('kzc',18))


#通过下标
p=['kzc',18]
print '{0[0]},{0[1]}'.format(p)


#格式限定符 - 填充与对齐
'''
填充常跟对齐一起使用
^、<、>分别是居中、左对齐、右对齐，后面带宽度
'''
print '{:>8}'.format('189')

print '{:0>8}'.format('189')  ##:号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充

print '{:a>8}'.format('189')


#精度与类型f
print '{:.2f}'.format(321.33345)  #.2表示长度为2的精度，f表示float类型


#进制
'''
b、d、o、x分别是二进制、十进制、八进制、十六进制
'''
print '{:b}'.format(17)

print '{:d}'.format(17)

print '0{:o}'.format(17)

print '0x{:x}'.format(17)


#金额千位分隔符
print '{:,}'.format(1234567890)


#其他
import sys
print "{0.platform}".format(sys)


'''
'!a'  (apply ascii())
'!s'  (apply str())
'!r'  (apply repr())
这些方法可以用来在格式化前转化数值
'''
import math
print repr(math.pi)
print('The value of PI is approximately {!r}.'.format(math.pi))

print str(math.pi)
print('The value of PI is approximately {!s}.'.format(math.pi))



#用**把字典作为关键字参数
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print("Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}".format(**table))
