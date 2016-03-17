#coding=utf8
"""
中介模式
定义：用一个中介对象封装一系列的对象交互，中介使各对象不需要显示地相互作用，从而使耦合松散，而且可以独立地改变它们之间的交互
类型：行为类模式
"""

class Mediator:
    def Send(self,message,col):
        pass

class Colleague:
    def __init__(self,temp):
        self.mediator = temp

class Colleague1(Colleague):
    def Send(self,message):
        self.mediator.Send(message,self)
    def Notify(self,message):
        print "Colleague1 get a message:%s" %message

class Colleague2(Colleague):
    def Send(self,message):
        self.mediator.Send(message,self)
    def Notify(self,message):
        print "Colleague2 get a message:%s" %message

class ConcreteMediator(Mediator):
    def Send(self,message,col):
        if(col==col1):
            col2.Notify(message)
        else:
            col1.Notify(message)

if __name__ == "__main__":
    m =ConcreteMediator()
    col1 = Colleague1(m)
    col2 = Colleague1(m)
    m.col1=col1
    m.col2=col2
    col1.Send("How are you?");
    col2.Send("Fine.");
