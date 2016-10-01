#coding=utf8
import itertools

#排列 组合
for i in itertools.combinations([1, 2, 3], 2):   #创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序 不带重复 combinations(iterable, r)
    print i


for i in itertools.combinations_with_replacement([1, 2, 3], 2):  #同上, 带重复
    print i


for i in itertools.product([1, 2, 3], [4, 5], [6, 7]):  #创建一个迭代器，生成表示item1，item2等中的项目的笛卡尔积的元组，repeat是一个关键字参数，指定重复生成序列的次数 product(iter1, iter2, ... iterN, [repeat=1])
    print i


for i in itertools.permutations([1, 2, 3], 3):  #返回p中任意取r个元素做排列的元组的迭代器 permutations(p[, r])
    print i
