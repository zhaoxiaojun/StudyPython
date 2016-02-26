#coding=utf8

def BubbleSort(L):
    '''
    冒泡排序
    '''
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

def SelectSort(L):
    '''
    选择排序
    '''
    n = len(L)
    for i in xrange(0,n):
        mii = i
        for j in xrange(i+1, n):
            if L[j] < L[mii]:
                mii = j
        if i != mii:
            L[mii], L[i] = L[i], L[mii]


def InsertSort(L):
    '''
    选择排序
    '''
    n = len(L)
    for i in xrange(1,n):
        tmp = L[i]
        j = i
        while j>0 and L[j-1] > tmp:
            L[j] = L[j-1]
            j = j-1
        L[j] = tmp


def merge_sort(a_list):
    '''
    合并排序
    '''
    print("Splitting ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i=0;j=0;k=0;
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i=i+1
            else:
                a_list[k] = right_half[j]
                j=j+1
            k=k+1
        while i < len(left_half):
            a_list[k] = left_half[i]
            i=i+1
            k=k+1
        while j < len(right_half):
            a_list[k] = right_half[j]
            j=j+1
            k=k+1
    print("Merging ", a_list)


def shell_sort(a_list):
    '''
    希尔排序
    '''
    #how many sublists, also how many elements in a sublist
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
    #start+gap is the second element in this sublist
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap] #move backward
            position = position - gap
            a_list[position] = current_value



def quick_sort(a_list):
    '''
    快速排序
    '''
    quick_sort_helper(a_list, 0, len(a_list) - 1)

def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)

def partition(a_list, first, last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp
    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp
    return right_mark




#桶排序


#基数排序


#计数排序


if __name__ == '__main__':
    L = [23,34,57,3,2,3,86,45,6,9]
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    #print L
    #BubbleSort(L)
    #SelectSort(L)
    #InsertSort(L)
    #merge_sort(L)
    #quick_sort(a_list)
    shell_sort(a_list)
    print(a_list)
    #print L
