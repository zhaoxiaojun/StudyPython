#coding=utf8
#Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):   #格式化一个邮件地址
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))  #.. if .. else .. 结构

#from_addr = raw_input('From: ')
#password = raw_input('Password: ')
#to_addr = raw_input('To: ')
#smtp_server = raw_input('SMTP server: ')
from_addr = 'yzh87117835@163.com'
password = '***'
to_addr = 'yechaohui@tuandai.com'
smtp_server = 'smtp.163.com'

#发送文本邮件
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

#发送HTML邮件
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')


msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()


server = smtplib.SMTP(smtp_server, 25)  #SMTP协议默认端口是25
#server.set_debuglevel(1)  #打印出和SMTP服务器交互的所有信息
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())  #可以一次发给多个人
server.quit()
