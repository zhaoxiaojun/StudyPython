#coding=utf8
import time
import datetime
'''
datetime模块定义了下面这几个类：
datetime.date：表示日期的类。常用的属性有year, month, day；
datetime.time：表示时间的类。常用的属性有hour, minute, second, microsecond；
datetime.datetime：表示日期时间。
datetime.timedelta：表示时间间隔，即两个时间点之间的长度。
datetime.tzinfo：与时区有关的相关信息。
'''

#date类
'''
datetime所能表达的时间范围：
    year的范围是[MINYEAR, MAXYEAR]，即[1, 9999]
    month的范围是[1, 12]。（月份是从1开始的，不是从0开始的~_~）
    day的最大值根据给定的year, month参数来决定。例如闰年2月份有29天
'''
print 'date.year:', datetime.date.year
print 'date.month:', datetime.date.month
print 'date.day:',datetime.date.day
print 'date.max:' , datetime.date.max #date对象所能表示的最大日期
print 'date.min:' , datetime.date.min #date对象所能表示的最小日期
print 'date.today():' , datetime.date.today() #返回一个表示当前本地日期的date对象
print 'date.fromtimestamp():' , datetime.date.fromtimestamp(time.time())  #根据给定的时间戮，返回一个date对象
print 'date对象表示日期的最小单位:', datetime.date.resolution
#print '将Gregorian日历时间转换为date对象:', datetime.fromordinal(ordinal)

now = datetime.date(2010, 04, 06)
tomorrow = now.replace(day=07)   #date.replace(year, month, day)  生成一个新的日期对象，用参数指定的年，月，日代替原有对象中的属性
print 'now:', now,  ', tomorrow:', tomorrow
print 'timetuple():', now.timetuple()  #返回日期对应的time.struct_time对象
print 'toordinal():', now.toordinal()  #返回日期对应的Gregorian Calendar日期
print 'weekday():', now.weekday() #返回weekday，如果是星期一，返回0；如果是星期2，返回1，以此类推
print 'isoweekday():', now.isoweekday() #返回weekday，如果是星期一，返回1；如果是星期2，返回2，以此类推
print 'isocalendar():', now.isocalendar()   #返回格式如(year，month，day)的元组
print 'isoformat():', now.isoformat()  #返回格式如'YYYY-MM-DD的字符串
print 'strftime():', now.strftime("%Y--%m--%d")  #返回自定义格式化字符串

delta = tomorrow - now   #两个日期相减，返回一个时间间隔对象
print  'timedelta:', delta
print  'date + timedelta', now + delta
print  '日期比较：', tomorrow > now


#timel类
'''
time类表示时间，由时、分、秒以及微秒组成。
time类的构造函数如下：
class datetime.time(hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ) ：
各参数的取值范围：hour的范围为[0, 24)，minute的范围为[0, 60)，second的范围为[0, 60)，microsecond的范围为[0, 1000000)。tzinfo表示时区信息。
'''
print 'time.min:', datetime.time.min  #time类所能表示的最小时间 time.min = time(0, 0, 0, 0)
print 'time.max:', datetime.time.max  #time类所能表示的最大时间 time.max = time(23, 59, 59, 999999)
print 'time.resolution:', datetime.time.resolution   #时间的最小单位 1微秒

tm = datetime.time(23, 46, 10)
print 'tm:', tm
print 'hour: %d, minute: %d, second: %d, microsecond: %d'  % (tm.hour, tm.minute, tm.second, tm.microsecond)   #时、分、秒、微秒
print 'time.tzinfo', tm.tzinfo  #时区信息
tm1 = tm.replace(hour=20)    #time.replace([ hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] ) 创建一个新的时间对象，用参数指定的时、分、秒、微秒代替原有对象中的属性
print 'tm1:' , tm1
print 'isoformat():' , tm.isoformat()  #返回型如"HH:MM:SS"格式的字符串表示
print 'strftime():', tm.strftime("%H--:%M--:%S")  #返回自定义格式化字符串


#datetime类
'''
datetime是date与time的结合体，包括date与time的所有信息
构造函数:
datetime.datetime (year, month, day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] )，各参数的含义与date、time的构造函数中的一样
'''
print   'datetime.max:' , datetime.datetime.max    #datetime所能表示的最大值
print   'datetime.min:' , datetime.datetime.min    #datetime所能表示的最小值
print   'datetime.resolution:' , datetime.datetime.resolution  #datetime最小单位
print   'today():' , datetime.datetime.today()  #返回一个表示当前本地时间的datetime对象
print   'now():' , datetime.datetime.now()  #datetime.now([tz]) 返回一个表示当前本地时间的datetime对象，如果提供了参数tz，则获取tz参数所指时区的本地时间
print   'utcnow():' , datetime.datetime.utcnow()  #返回一个当前utc时间的datetime对象
print   'fromtimestamp(tmstmp):' , datetime.datetime.fromtimestamp(time.time())   #datetime.fromtimestamp(timestamp[, tz])  根据时间戮创建一个datetime对象，参数tz指定时区信息
print   'utcfromtimestamp(tmstmp):' , datetime.datetime.utcfromtimestamp(time.time()) #根据时间戮创建一个datetime对象
# datetime.combine(date, time)：根据date和time，创建一个datetime对象
# datetime.strptime(date_string, format)：将格式字符串转换为datetime对象

dnow = datetime.datetime(2010, 04, 06, 23, 46, 10, 473000)
print 'dnow:', dnow
print 'datetime.year:', dnow.year
print 'datetime.month:', dnow.month
print 'datetime.day:', dnow.day
print 'datetime.hour:', dnow.hour
print 'datetime.minute:', dnow.minute
print 'datetime.second:', dnow.second
print 'datetime.microsecond:', dnow.microsecond
print 'datetime.tzinfo:', dnow.tzinfo

print dnow.date()  #获取date对象；
print dnow.time()  #获取time对象；
dnow1 = dnow.replace(year=2015, hour=11)  #datetime. replace ([ year[ , month[ , day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] ] ] ])
print 'dnow1:',dnow1
print 'timetuple():', dnow.timetuple()
print 'utctimetuple():', dnow.utctimetuple()
print 'toordinal():', dnow.toordinal()
print 'weekday():', dnow.weekday()
print 'isoweekday():', dnow.isoweekday()
print 'isocalendar():', dnow.isocalendar()
print 'isoformat():', dnow.isoformat()
print 'strftime():', dnow.strftime("%Y--%m--%d %H--:%M--:%S")
print 'ctime():', dnow.ctime()  #返回一个日期时间的C格式字符串，等效于time.ctime(time.mktime(dt.timetuple()))

#datetime、date、time对象都提供了strftime()方法，该方法接收一个格式字符串，输出日期时间的字符串表示。包含的格式：
'''
%a 星期的简写。如 星期三为Web
%A 星期的全写。如 星期三为Wednesday
%b 月份的简写。如4月份为Apr
%B月份的全写。如4月份为April
%c:  日期时间的字符串表示。（如： 04/07/10 10:43:39）
%d:  日在这个月中的天数（是这个月的第几天）
%f:  微秒（范围[0,999999]）
%H:  小时（24小时制，[0, 23]）
%I:  小时（12小时制，[0, 11]）
%j:  日在年中的天数 [001,366]（是当年的第几天）
%m:  月份（[01,12]）
%M:  分钟（[00,59]）
%p:  AM或者PM
%S:  秒（范围为[00,61]，为什么不是[00, 59]，参考python手册~_~）
%U:  周在当年的周数当年的第几周），星期天作为周的第一天
%w:  今天在这周的天数，范围为[0, 6]，6表示星期天
%W:  周在当年的周数（是当年的第几周），星期一作为周的第一天
%x:  日期字符串（如：04/07/10）
%X:  时间字符串（如：10:43:39）
%y:  2个数字表示的年份
%Y:  4个数字表示的年份
%z:  与utc时间的间隔 （如果是本地时间，返回空字符串）
%Z:  时区名称（如果是本地时间，返回空字符串）
%%:  %% => %
'''

dt = datetime.datetime.now()
print '(%Y-%m-%d %H:%M:%S %f): ' , dt.strftime('%Y-%m-%d %H:%M:%S %f')
print '(%Y-%m-%d %H:%M:%S %p): ' , dt.strftime('%y-%m-%d %I:%M:%S %p')
print '%%a: %s '  % dt.strftime('%a')
print '%%A: %s '  % dt.strftime('%A')
print '%%b: %s '  % dt.strftime('%b')
print '%%B: %s '  % dt.strftime('%B')
print '日期时间%%c: %s '  % dt.strftime('%c')
print '日期%%x：%s '  % dt.strftime('%x')
print '时间%%X：%s '  % dt.strftime('%X')
print '今天是这周的第%s天 '  % dt.strftime('%w')
print '今天是今年的第%s天 '  % dt.strftime('%j')
print '今周是今年的第%s周 '  % dt.strftime('%U')
