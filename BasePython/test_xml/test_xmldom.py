#coding=utf-8
import xml.dom.minidom as minidom

dom = minidom.parse("E:\\Code\\yzhPython\\testpy\\test.xml")   #得到dom对象
#dom = xml.dom.minidom.parseString(xmlstring)   #从xml字符串得到dom对象

#root = dom.documentElement   #得到文档元素对象
root = dom.getElementsByTagName("Schools")  #根据元素名称得到子元素文档对象（列表）

print root.length  #Schools子元素文档对象个数
print root[0].toxml()   #打印root[0]表示的xml

for node in root: 
    print "Root element is %s"  % node.tagName  #根节点元素名
    schools = node.getElementsByTagName("School")   #根据元素名称得到子元素文档对象   
    for school in schools:
        print school.nodeName   #节点名
        #print school.tagName
        print school.getAttribute("Name")   #节点Name属性值
        #print school.attributes["Name"].value
        print school.nodeType   #结点的类型,1为ELEMENT_NODE
        print school.nodeValue  #结点的值，只对文本结点TEXT_NODE有效
        
        classes = school.getElementsByTagName("Class")  #根据元素名称得到子元素文档对象
        print "There are %d classes in school %s" %(classes.length, school.getAttribute("Name"))
        for mclass in classes:
            print mclass.getAttribute("Id")  #节点Id属性值
            
            for student in mclass.getElementsByTagName("Student"):
                print student.attributes["Name"].value
                print student.getElementsByTagName("English")[0].childNodes[0].nodeValue
                