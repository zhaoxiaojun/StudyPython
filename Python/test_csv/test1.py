#coding=utf8
#读数据
import csv
from collections import namedtuple

with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)  #Python 2.6+有内建函数next(iterator) 相当于迭代器next方法it.next()
    print headers
    print ''
    for row in f_csv:
        print row
        #print row[0]
        #print type(row)  #list
    print ''


#下标访问通常会引起混淆，可以考虑使用命名元组（缺点也很明显）
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        print row.Symbol
    print ''


#将数据读取到一个字典序列中
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print row



