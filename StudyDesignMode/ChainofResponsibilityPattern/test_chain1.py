#coding=utf8
"""
职责链模式（责任链模式）
定义：使多个对象都有机会处理请求，从而避免了请求的发送者和接收者之间的耦合关系。将这些对象连成一条链，并沿着这条链传递该请求，直到有对象处理它为止
类型：行为类模式
"""

#请假和加薪等请求发给上级，如果上级无权决定，那么递交给上级的上级

class Request:
    def __init__(self,tcontent,tnum):
        self.content = tcontent
        self.num = tnum

class Manager:
    def __init__(self,name):
        self.name = name
    def SetSuccessor(self,manager):
        self.manager = manager
    def GetRequest(self,req):
        pass

class CommonManager(Manager):
    def GetRequest(self,req):
        if(req.num>=0 and req.num<10):
            print "%s handled %d request." %(self.name,req.num)
        else:
            self.manager.GetRequest(req)

class MajorDomo(Manager):
    def GetRequest(self,req):
        if(req.num>=10):
            print "%s handled %d request." %(self.name,req.num)

if __name__ == "__main__":
    common = CommonManager("Zhang")
    major = MajorDomo("Lee")
    common.SetSuccessor(major)
    req = Request("rest",33)
    common.GetRequest(req)
    req2 = Request("salary",3)
    common.GetRequest(req2)
