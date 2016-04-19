#coding=utf8
import time
import datetime

#当前时间戳
t = time.time()  #1970.1.1 到现在经过的秒数
print t
now = time.localtime() #或：now = time.localtime(time.time())   struct_time类型
print now
print time.gmtime(t)  #时间戳转为struct_time类型
print time.mktime(now)   #struct_time类型转为时间戳

#将时间值转化为字符串
now = time.localtime()
print time.asctime(now)
print time.strftime("%y/%m/%d %H:%M", now)
print time.strftime("%a %b %d", now)
print time.strftime("%c", now)


#将时间字符串转化为时间戳
a = "2013-10-10 23:40:00"
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
timeStamp = int(time.mktime(timeArray))
print timeStamp


#时间字符串格式更改,如a = "2013-10-10 23:40:00",想改为 a = "2013/10/10 23:40:00"
# 方法:先转换为时间数组,然后转换为其他格式
a = "2013-10-10 23:40:00"
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
print otherStyleTime

#将时间戳转换为指定格式日期
# 方法一: 利用localtime()转换为时间数组,然后格式化为需要的格式
timeStamp = 1381419600
timeArray = time.localtime(timeStamp)
otherStyleTime1 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print "otherStyletime1",otherStyleTime1

# 方法二:
timeStamp = 1381419600
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime2 = dateArray.strftime("%Y-%m-%d %H:%M:%S")
print "otherStyletime2",otherStyleTime2


#获取当前时间并转换为指定日期格式
# 方法一:
now = time.time()  #获得当前时间时间戳
timeArray = time.localtime(now)
otherStyleTime3 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print "otherStyleTime3:",otherStyleTime3

# 方法二:
now = datetime.datetime.now()  #这是时间数组格式
otherStyleTime4 = now.strftime("%Y-%m-%d %H:%M:%S")
print "otherStyleTime4:",otherStyleTime4

# 方法三
now = time.strftime("%Y-%m-%d %H:%M:%S")
print "now:",now


#获得当前的三天前的时间
threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 3))   #注:timedelta()的参数有:days,hours,seconds,microseconds
timeStamp = int(time.mktime(threeDayAgo.timetuple()))   #转换为时间戳
otherStyleTime5 = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")  #转换为其他字符串格式
print otherStyleTime5


#给定时间戳,计算该时间戳对应时间的三天前的时间:
timeStamp = 1381419600
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
threeDayAgo = dateArray - datetime.timedelta(days = 3)
print threeDayAgo
