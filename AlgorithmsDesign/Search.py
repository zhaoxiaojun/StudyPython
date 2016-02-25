#coding=utf8
#查找


#二分查找
def Binary_Search(L, key):
    low = 0
    hight = len(L)-1
    while low<=hight:
        mid = (low+hight)/2
        if L[mid]>key:
            hight = mid-1
        elif L[mid]<key:
            low = mid+1
        else:
            return mid
    return -1




if __name__ == '__main__':
    L = [23,34,57,3,2,3,86,45,6,9]
    L.sort()
    key = 86
    print L
    print Binary_Search(L, key)
