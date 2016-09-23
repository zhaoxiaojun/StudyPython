#coding=utf8
#时间转换
import time
import datetime


a = "2013-10-01"
timeArray = time.strptime(a, "%Y-%m-%d")
timeStamp = int(time.mktime(timeArray))
print timeStamp


timeStamp = 0
timeArray = time.localtime(timeStamp)
otherStyleTime1 = time.strftime("%H:%M:%S", timeArray)
print "otherStyletime1",otherStyleTime1



def change_time(time_str):
    timeArray = time.strptime(time_str, "%Y-%m-%d")
    timeStamp = int(time.mktime(timeArray))
    timeStamp = int(str(timeStamp) + '000000')
    return timeStamp

a = "2013-10-01"
b = change_time(a)
print b
