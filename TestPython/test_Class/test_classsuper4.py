#coding=utf8

#不要一说到 super 就想到父类！super 指的是 MRO 中的下一个类！
def super(cls, inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls)+1]
'''
super 其实干的是这件事：
inst负责生成MRO的list
通过cls定位当前MRO中的index，并返回mro[index+1]
MRO: Method Resolution Order 代表了类继承的顺序
'''
