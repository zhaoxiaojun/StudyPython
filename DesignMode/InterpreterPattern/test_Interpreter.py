#coding=utf8
"""
解释器模式
定义：给定一种语言，定义他的文法的一种表示，并定义一个解释器，该解释器使用该表示来解释语言中句子
类型：行为类模式
"""

class Context:
    def __init__(self):
        self.input=""
        self.output=""

class AbstractExpression:
    def Interpret(self,context):
        pass

class Expression(AbstractExpression):
    def Interpret(self,context):
        print "terminal interpret"

class NonterminalExpression(AbstractExpression):
    def Interpret(self,context):
        print "Nonterminal interpret"

if __name__ == "__main__":
    context= ""
    c = []
    c = c + [Expression()]
    c = c + [NonterminalExpression()]
    c = c + [Expression()]
    c = c + [Expression()]
    for a in c:
        a.Interpret(context)
