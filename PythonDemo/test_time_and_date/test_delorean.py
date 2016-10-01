#coding=utf8
#好用的日期时间处理
from delorean import Delorean

EST = "US/Eastern"

d = Delorean(timezone=EST)

print d
