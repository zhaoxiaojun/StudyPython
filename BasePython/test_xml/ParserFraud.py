#coding=utf8
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

'''
每个element对象都具有以下属性：
1. tag：string对象，表示数据代表的种类
2. attrib：dictionary对象，表示附有的属性
3. text：string对象，表示element的内容
4. tail：string对象，表示element闭合之后的尾迹
5. 若干子元素（child elements）
<tag attrib1=1>text</tag>tail
  1     2        3         4
'''




#root = ET.fromstring(country_data_as_string) ＃从字符串读取数据

#从xml文件读取数据
tree = ET.parse("TestFraud.xml")
root = tree.getroot()
# 或：
# from xml.etree.ElementTree import ElementTree
# tree = ElementTree()
# tree.parse("TestFraud.xml")
# root = tree.getroot()

print root.tag
print root.attrib

# for child in root:
#     print child.tag, child.attrib

print root[0].tag
print root[0].attrib

childrenlist = root.getchildren()
print childrenlist[1].get("name")  #获取属性值

classes = childrenlist[1].findall(".")  #XPath
print classes

print classes[0].items() #根据属性字典返回一个列表
print classes[0].keys()  #返回包含所有元素属性键的列表
print classes[0].attrib['id']
print '=============================='

po = classes[0].find("pageo")
print po.text
print '=============================='

stepsele = classes[0].find("steps")
print len(stepsele)

#深度遍历
print stepsele.itertext().next()

print '----'
#itersep = stepsele.iter("step")
itersep = stepsele.iterfind("step")
print itersep.next()
print itersep.next()
print list(itersep)

for ele in stepsele:
    print '---'
    print ele
    print ele.attrib['comment']
    print ele.findtext("operation")
    print ele.findtext("value")
print '=============================='

assertele = classes[0].find("assert")
print assertele.findtext("assertmethod")
print assertele.findtext("checkmethod")
print assertele.findtext("exp")
