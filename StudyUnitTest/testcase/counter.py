#coding=utf-8

#计算器类
class counter:
    def __init__(self):
        self.values = 0
    
    def add(self,x,y):
        self.values = x + y
        return self.values
    
    def subtraction(self,x,y):
        self.values = x - y
        return self.values
        
    
if __name__ == '__main__':
    counterd = counter()
    print counterd.add(1,1)
    print counterd.subtraction(1, 1)