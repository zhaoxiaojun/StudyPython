#coding=utf8
#用法：

def func(a, b):
    return a / b


if __name__ == '__main__':
    import sys
    import traceback
    try:
        func(1, 0)
    except Exception as e:
        print "print exc"
        #traceback.print_exc(file=sys.stdout)
        traceback.print_exc()
