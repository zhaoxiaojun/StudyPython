#coding=utf8
import  xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse('abc.xml')

#得到文档元素对象
root = dom.documentElement


print root.nodeName   #结点名字
print root.nodeValue  #结点的值，只对文本结点有效
print root.nodeType  #XML DOM节点类型值 http://www.w3school.com.cn/xmldom/dom_nodetype.asp
#print root.ELEMENT_NODE

#获得子标签
bb = root.getElementsByTagName('maxid')
print bb
b= bb[0]
print b
print b.nodeName

bb = root.getElementsByTagName('caption')   #多个相同标签名字的标签
print bb
b= bb[2]
print b
print b.nodeName
print 'data: ',b.firstChild.data   #标签对之间的数据


#获得标签属性值
itemlist = root.getElementsByTagName('login')
item = itemlist[0]
un = item.getAttribute("username")
print 'username',un
pd = item.getAttribute("passwd")
print 'passwd',pd



