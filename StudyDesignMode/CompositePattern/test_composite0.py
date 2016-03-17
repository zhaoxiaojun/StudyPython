#coding=utf8
"""
组合模式
定义：将对象以树形结构组织起来，以达成“部分－整体” 的层次结构，使得客户端对单个对象和组合对象的使用具有一致性
"""

#公司人员的组织结构

class Component:
    def __init__(self,strName):
        self.m_strName = strName
    def Add(self,com):
        pass
    def Display(self,nDepth):
        pass

class Leaf(Component):
    def Add(self,com):
        print "leaf can't add"
    def Display(self,nDepth):
        strtemp = ""
        for i in range(nDepth):
            strtemp=strtemp+"-"
        strtemp=strtemp+self.m_strName
        print strtemp

class Composite(Component):
    def __init__(self,strName):
        self.m_strName = strName
        self.c = []
    def Add(self,com):
        self.c.append(com)
    def Display(self,nDepth):
        strtemp=""
        for i in range(nDepth):
            strtemp=strtemp+"-"
        strtemp=strtemp+self.m_strName
        print strtemp
        for com in self.c:
            com.Display(nDepth+2)

if __name__ == "__main__":
    p = Composite("Wong")
    p.Add(Leaf("Lee"))
    p.Add(Leaf("Zhao"))
    p1 = Composite("Wu")
    p1.Add(Leaf("San"))
    p.Add(p1)
    p.Display(1);
