#coding=utf8
"""
桥接模式
定义：将抽象和行为划分开来，各自独立，但能动态的结合
"""

#两种品牌的手机，要求它们都可以运行游戏和通讯录两个软件，而不是为每个品牌的手机都独立编写不同的软件

class HandsetSoft(object):
    def Run(self):
        pass

class HandsetGame(HandsetSoft):
    def Run(self):
        print "Game"

class HandsetAddressList(HandsetSoft):
    def Run(self):
        print "Address List"

class HandsetBrand(object):
    def __init__(self):
        self.m_soft = None
    def SetHandsetSoft(self,temp):
        self.m_soft= temp
    def Run(self):
        pass

class HandsetBrandM(HandsetBrand):
    def Run(self):
        if not (self.m_soft == None):
            print "BrandM"
            self.m_soft.Run()

class HandsetBrandN(HandsetBrand):
    def Run(self):
        if not (self.m_soft == None):
            print "BrandN"
            self.m_soft.Run()

if __name__ == "__main__":
    brand = HandsetBrandM()
    brand.SetHandsetSoft(HandsetGame())
    brand.Run()
    brand.SetHandsetSoft(HandsetAddressList())
    brand.Run()
