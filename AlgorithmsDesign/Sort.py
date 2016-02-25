#coding=utf8

#冒泡排序
def BubbleSort(L):
    n = len(L)
    flag = True
    while flag and n>0:
        flag = False
        for i in xrange(1,n):
            for j in xrange(0,n-i):
                if L[j] > L[j+1]:
                    flag = True
                    # tmp = L[j]
                    # L[j] = L[j+1]
                    # L[j+1] = tmp
                    L[j], L[j+1] = L[j+1], L[j]

#选择排序
def SelectSort(L):
    n = len(L)
    for i in xrange(0,n):
        mii = i
        for j in xrange(i+1, n):
            if L[j] < L[mii]:
                mii = j
        if i != mii:
            L[mii], L[i] = L[i], L[mii]


#直接插入排序
def InsertSort(L):
    n = len(L)
    for i in xrange(1,n):
        if L[i] < L[i-1]:
            tmp = L[i]
            j = i-1
            while L[j] > tmp:
                print j
                L[j+1] = L[j]
                j = j-1
            L[j+1] = tmp



if __name__ == '__main__':
    L = [23,34,57,3,2,3,86,45,6,9]
    print L
    #BubbleSort(L)
    #SelectSort(L)
    InsertSort(L)
    print L
