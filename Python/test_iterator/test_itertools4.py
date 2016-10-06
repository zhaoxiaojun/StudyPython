#coding=utf8


'''
compress(data, selectors)
如果bool(selectors[n])为True，则next()返回data[n]，否则跳过data[n]。
compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F

dropwhile(pred, seq)
当pred对seq[n]的调用返回False时才开始迭代。
dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1

ifilterfalse(pred, seq)
ifilter的相反版本。
ifilterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8

starmap(func, seq)
将seq的每个元素以变长参数(*args)的形式调用func。
starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000

izip_longest(p, q, ..., fillvalue=None)
izip的取最长序列的版本，短序列将填入fillvalue。
izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
'''
