#coding=utf8
#解析MIMEText对象

import sys, email, time
from email import Utils


fp = open('email.data', 'r+')
msg = email.message_from_file(fp)

print '***Header in massage: '
for header, value in msg.items():
    print header + ':'
    print " " + value

if msg.is_multipart():
    print 'this program can not handler MIME multipart message!'
    sys.exit(-1)



#特定头
print '-'*60
if 'subject' in msg:
    print 'Subject: ', msg['subject']
print '-'*60

print 'Message Body: \n'
print msg.get_payload()

#解析日期
print '-'*60
if 'date' not in msg:
    exit(-1)
datehdr = msg['date'].strip()
print datehdr
dateval = Utils.mktime_tz(Utils.parsedate_tz(datehdr))
print dateval

print 'Message was sent on', time.strftime("%A, %B %d %Y at %I:%M %p", time.localtime(dateval))
