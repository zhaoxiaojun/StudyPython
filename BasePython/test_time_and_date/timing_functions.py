#coding=utf8
#被测程序
import random


#不需要在代码中用import导入模块line_profiler
@profile
def random_sort2(n):
    l = [random.random() for i in range(n)]
    l.sort()
    return l

if __name__ == "__main__":
    random_sort2(2000000)
