#coding=utf8
"""
序列
C.__len__(self) 序列中项的数目
C.__getitem__(self, ind) 得到单个序列元素
C.__setitem__(self, ind,val) 设置单个序列元素
C.__delitem__(self, ind) 删除单个序列元素

C.__getslice__(self, ind1,ind2) 得到序列片断
C.__setslice__(self, i1, i2,val) 设置序列片断
C.__delslice__(self, ind1,ind2) 删除序列片断
C.__contains__(self, val) f 测试序列成员；内建in 关键字
C.__*add__(self,obj) 串连；+操作符
C.__*mul__(self,obj) 重复；*操作符
C.__iter__(self)  创建迭代类；内建iter()
"""

class A(object):
    def __init__(self):
        print "call __init__"
        self.value = [1,2,3,4,5,6]

    def __len__(self):
        print "call __len__"
        return len(self.value)

    def __getitem__(self, index):
        print "call __getitem__"
        return self.value[index]

    def __setitem__(self, index, value):
        print "call __setitem__"
        self.value[index] = value

    def __delitem__(self, index):
        print "call __delitem__"
        del self.value[index]

if __name__ == '__main__':
    a = A()
    print len(a)
    print a[2]
    a[2] = 99
    del a[2]
