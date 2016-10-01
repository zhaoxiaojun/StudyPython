#coding=utf8

#指定步长切割列表
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print a[::2]
print a[::3]
print a[2:8:2]


#负数步长切割列表
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print a[::-1]
print a[::-2]



#列表切割赋值
a = [1, 2, 3, 4, 5]
a[2:3] = [0, 0]
print a
a[1:1] = [8, 9]
print a
a[1:-1] = []
print a


#命名列表切割方式
a = [0, 1, 2, 3, 4, 5]
LASTTHREE = slice(-3, None)
LASTTHREE  #slice(-3, None, None)
print a[LASTTHREE]


#滑动取值窗口
def n_grams(a, n):
    z = [iter(a[i:]) for i in range(n)]
    return zip(*z)

a = [1, 2, 3, 4, 5, 6]
print n_grams(a, 2)
print n_grams(a, 3)
print n_grams(a, 4)

