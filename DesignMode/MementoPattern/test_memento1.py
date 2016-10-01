#coding=utf8
"""
备忘录模式
定义：在不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态。这样就可以将该对象恢复到原先保存的状态
类型：行为类
"""

#将Originator对象的状态封装成Memo对象保存在Caretaker内

class Originator:
    def __init__(self):
        self.state = ""
    def Show(self):
        print self.state
    def CreateMemo(self):
        return Memo(self.state)
    def SetMemo(self,memo):
        self.state = memo.state

class Memo:
    state= ""
    def __init__(self,ts):
        self.state = ts

class Caretaker:
    memo = ""

if __name__ == "__main__":
    on = Originator()
    on.state = "on"
    on.Show()
    c = Caretaker()
    c.memo=on.CreateMemo()
    on.state="off"
    on.Show()
    on.SetMemo(c.memo)
    on.Show()


