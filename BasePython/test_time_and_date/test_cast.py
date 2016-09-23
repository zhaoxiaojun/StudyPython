#coding=utf8
#统计时间消耗的方法
import time
import timeit

def test(n):
    """Stupid test function"""
    L = []
    for i in range(n):
        L.append(i)

if __name__ == '__main__':
    test_round = 1000
    #方法1：自带计时框架
    time_cost = timeit.timeit("test(10000)", setup="from __main__ import test", number = test_round)
    print "time_cost: ", time_cost
    print "avg_cost: ", time_cost/test_round

    #方法2：手工计算时间差
    time_start = time.clock()
    for i in range(0,test_round):
        test(10000)
    time_end = time.clock()
    time_cost2 = (time_end - time_start)/test_round
    print 'time_cost: ',time_end - time_start
    print "avg_cost: ", time_cost2

    #方法3：手工计算时间差
    time_start = time.time()
    for i in range(0,test_round):
        test(10000)
    time_end = time.time()
    time_cost3 = (time_end - time_start)/test_round
    print 'time_cost: ',time_end - time_start
    print "avg_cost: ", time_cost3

    #方法4：通过外部shell命令time
    #time -p python timing_functions.py
    '''
    real表示的是执行脚本的总时间
    user表示的是执行脚本消耗的CPU时间
    sys表示的是执行内核函数消耗的时间
    real执行时间和user+sys执行时间的差就是消耗在输入/输出和系统执行其他任务时消耗的时间
    '''

    #方法5：通过python命令cProfile模块
    #如果想知道每个函数和方法消耗了多少时间，以及这些函数被调用了多少次，可以使用cProfile模块
    #python -m cProfile -s cumulative timing_functions.py   -s选项（累加）最终结果会根据每个函数的累计执行时间排序
    #貌似有BUG，执行本文件会报错


    #方法6：line_profiler模块
    #给出执行每行代码所需占用的CPU时间  安装： pip install line_profiler
    #命令行执行：kernprof -l -v timing_functions.py
    #其中-l表示逐行解释，-v表示表示输出详细结果。通过这种方法，我们看到构建数组消耗了44%的计算时间，而sort()方法消耗了剩余的56%的时间




