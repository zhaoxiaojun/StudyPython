#coding=utf8
"""
打印列表各项，列表中包含列表项时进行递归打印

"""

def print_lll(L):
    '''
    打印
    '''
    for i in L:
        if isinstance(i, list):
	    print_lll(i)
        else:
            print(i)

if __name__ == '__main__':
    L = ['sdf','fgh',12, 34,['ar','sd',12,3],'dfg']
    print_lll(L)
