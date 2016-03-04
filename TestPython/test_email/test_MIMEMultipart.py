#coding=utf8
#建立MIMEMultipart对象
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.mime.application import MIMEApplication
from email import Utils, Encoders

# def alternative(data, contenttype):
#     maintype, subtype = contenttype.split('/')
#     if maintype == 'text':
#         retval = MIMEText(data, _subtype=subtype)
#     else:
#         retval = MIMEBase(maintype, subtype)
#         retval.set_payload(data)
#         Encoders.encode_base64(retval)
#     return retval
#msg.attach(alternative(messagetext, 'text/plain'))
#msg.attach(alternative(messagehtml, 'text/html'))

msg = MIMEMultipart('alternative')
msg['From'] = 'yechaohui@tuandai.com'
msg['To'] = 'Test Sender <yechaohui@tuandai.com>'
msg['Subject'] = u'来自test_MIMEText.py的问候…'
msg['Date'] = Utils.formatdate(localtime = 1)
msg['Message-ID'] = Utils.make_msgid()

#文字部分
messagetext = '''Hello,
This is a test massage from test_MIMEText.py
'''
parttext = MIMEText(messagetext)
msg.attach(parttext)

#text/html
# messagehtml = '''<html><body><h1>Hello</h1>
# <p>send by <a href="http://www.python.org">Python</a>...</p>
# </body></html>'''

# retval = MIMEBase("text", "html")
# retval.set_payload(messagehtml)
# Encoders.encode_base64(retval)
# msg.attach(retval)

#文件类型附件
filepart = MIMEApplication(open('email.data','rb').read())
filepart.add_header('Content-Disposition', 'attachment', filename="email.data")
msg.attach(filepart)


print msg.as_string()

###########################################################################################
#邮件发送
import smtplib, socket

#from_addr = 'yzh87117835@163.com'
#password = 'mC7uE5wJ_8528'
from_addr = 'yechaohui@tuandai.com'
password = 'mC7uE5wJ_123456'
to_addr = 'yechaohui@tuandai.com'
#smtp_server = 'smtp.163.com'
smtp_server = 'smtp.exmail.qq.com'

try:
    server = smtplib.SMTP(smtp_server, 25)  #SMTP协议默认端口是25
    ehlocode = server.ehlo()[0]  #来自SMTP服务器数据形式的结果代码 正常:200~299
    useESMTP = 1
    if not (200 <= ehlocode <= 299):
        useESMTP = 0
        helocode = server.helo()[0]
        if not (200 <= helocode <= 299):
            raise SMTPHeloError(helocode, resp)

        print "Negotiating TLS ..."
        server.starttls()  #初始化加密信道
        ehlocode = server.ehlo()[0]
        if not (200 <= ehlocode <= 299):
            print "Couldn't EHLO after starttls"
            sys.exit(5)
        print "Using TLS connection "
    else:
        print "Server does not support TLS, using normal connection"

    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())  #可以一次发给多个人

except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
    print '*** Your message may not hava been sent!'
    print e
else:
    print 'Message successfully sent'
