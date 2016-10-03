#coding=utf8

"""
str.translate(table[, deletechars])

translate()方法根据参数table给出的表(包含256个字符)转换字符串的字符, 要过滤掉的字符放到deletechars参数中
table -- 翻译表，翻译表是通过maketrans方法转换而来。
deletechars -- 字符串中要过滤的字符列表。

"""
from string import maketrans

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

strr = "this is string example....wow!!!"
print strr.translate(trantab, 'xm')  #去除字符串中的'x'和'm'字符，剩下的字符进行装换

