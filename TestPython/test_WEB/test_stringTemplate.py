#coding=utf8
from string import Template

datastr = "我的名子叫${name},我的年龄是${age}"

#直接传递数据
s = Template("There $ac and $bc")
print s.substitute(ac='apple',bc='banana')  #substitute是一个严肃的方法，如果有key没有输入，那就一定会报错
print s.safe_substitute(ac='apple',bc='banbana')  #safe_substitute则不会报错，而是将$xxx直接输入到结果字符串中

#通过字典传递数据
datamap = {'name':"hello", 'age':"100"}
dtemp = Template(datastr)
result = dtemp.substitute(datamap)
print result


#定制变量符号
class MyTemplate(Template):
    delimiter = "#"
    #idpattern = "[a][_a-z0-9]*"

def Mytest():
  s = '#{aa}sdf is not #{ab}sdf'
  t = MyTemplate(s)
  d = {'aa':'apple','ab':'banbana'}
  print t.substitute(d)

Mytest()
