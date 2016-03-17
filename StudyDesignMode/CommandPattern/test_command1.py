#coding=utf8
"""
命令模式
定义：将一个请求封装成一个对象，从而让你使用不同的请求把客户端参数化，对请求排队或者记录请求日志，可以提供命令的撤销和恢复功能
类型：行为类模式
"""

#烧烤店有两种食物，羊肉串和鸡翅。客户向服务员点单，服务员将点好的单告诉大厨，由大厨进行烹饪

class Barbucer:
    def MakeMutton(self):
        print "Mutton"
    def MakeChickenWing(self):
        print "Chicken Wing"

class Command:
    def __init__(self,temp):
        self.receiver=temp
    def ExecuteCmd(self):
        pass

class BakeMuttonCmd(Command):
    def ExecuteCmd(self):
        self.receiver.MakeMutton()

class ChickenWingCmd(Command):
    def ExecuteCmd(self):
        self.receiver.MakeChickenWing()

class Waiter:
    def __init__(self):
        self.order =[]
    def SetCmd(self,command):
        self.order.append(command)
        print "Add Order"
    def Notify(self):
        for cmd in self.order:
            #self.order.remove(cmd)
            #lead to a bug
            cmd.ExecuteCmd()


if __name__ == "__main__":
    barbucer=Barbucer()
    cmd=BakeMuttonCmd(barbucer)
    cmd2=ChickenWingCmd(barbucer)
    girl=Waiter()
    girl.SetCmd(cmd)
    girl.SetCmd(cmd2)
    girl.Notify()
