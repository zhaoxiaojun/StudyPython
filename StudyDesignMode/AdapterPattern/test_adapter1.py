#coding=utf8
"""
适配器模式
定义：将两个不兼容的类纠合在一起使用，属于结构型模式，需要有Adaptee(被适配者)和Adaptor(适配器)两个身份
"""
class Target:
    def Request():
        print "common request."

class Adaptee(Target):
    def SpecificRequest(self):
        print "specific request."

class Adapter(Target):
    def __init__(self,ada):
        self.adaptee = ada
    def Request(self):
        self.adaptee.SpecificRequest()

if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    adapter.Request()
