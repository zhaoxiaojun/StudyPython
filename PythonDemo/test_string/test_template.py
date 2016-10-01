#coding=utf8
import string
"""
字符串模板方法
"""

new_style = string.Template('this is a $thing, it cost $$5')
print new_style.substitute({'thing':'book'})
print new_style.substitute(thing='desk')


new_style2 = 'this is a %(thing)s'
print new_style2 % {'thing':'cookes'}



msg =  string.Template('the sqaure of $number is $sqaure')
#利用locals函数传递参数
for number in range(10):
    sqaure = number * number
    print msg.substitute(locals())

#直接传递
for i in range(10):
    print msg.substitute(number=i, sqaure=i*i)
