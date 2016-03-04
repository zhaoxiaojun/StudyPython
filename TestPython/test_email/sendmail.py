#coding=utf8
#Python对SMTP支持有smtplib和email两个模块，email负责构造邮件（或解析邮件内容），smtplib负责发送邮件
from email import encoders
from email.header import Header
#from email.mime.text import MIMEText
from email.MIMEText import MIMEText
from email.utils import parseaddr, formataddr

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
password = 'mC7uE5wJ_8528'
to_addr = 'yechaohui@tuandai.com'
smtp_server = 'smtp.163.com'

#发送文本邮件
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

#发送HTML邮件
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')


msg['From'] = _format_addr(u'测试邮件 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

###########################################################################################
#邮件发送
import smtplib, socket

try:
    server = smtplib.SMTP(smtp_server, 25)  #SMTP协议默认端口是25
    ehlocode = server.ehlo()[0]  #来自SMTP服务器数据形式的结果代码 正常:200~299
    print ehlocode

    useESMTP = 1
    if not (200 <= ehlocode <= 299):
        useESMTP = 0
        helocode = server.helo()[0]
        if not (200 <= helocode <= 299):
            raise SMTPHeloError(helocode, resp)

    if useESMTP and server.has_extn('starttls'):
        if server.has_extn('size'):
            print 'Maximum message size is: ', server.esmtp_features['size']  #服务器允许的最大邮件容量

        print "Negotiating TLS ..."
        server.starttls()  #初始化加密信道
        ehlocode = server.ehlo()[0]
        if not (200 <= ehlocode <= 299):
            print "Couldn't EHLO after starttls"
            sys.exit(5)
        print "Using TLS connection "
    else:
        print "Server does not support TLS, using normal connection"

    #server.set_debuglevel(1)  #打印出和SMTP服务器交互的所有信息
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())  #可以一次发给多个人

except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
    print '*** Your message may not hava been sent!'
    print e
else:
    print 'Message successfully sent'


"""
socket.gaierror  寻找地址的时候出现错误
socket.error  普通IO和通信问题
socket.herror  其他地址错误
smtplib.SMTPException  SMTP会话错误

smtp协议的基本命令包括：
    HELO 向服务器标识用户身份
    MAIL 初始化邮件传输 mail from:
    RCPT 标识单个的邮件接收人；常在MAIL命令后面,可有多个rcpt to:
    DATA 在单个或多个RCPT命令后,表示所有的邮件接收人已标识,并初始化数据传输,以.结束
    VRFY 用于验证指定的用户/邮箱是否存在；由于安全方面的原因,服务器常禁止此命令
    EXPN 验证给定的邮箱列表是否存在,扩充邮箱列表,也常被禁用
    HELP 查询服务器支持什么命令
    NOOP 无操作,服务器应响应OK
    QUIT 结束会话
    RSET 重置会话,当前传输被取消
    MAIL FROM 指定发送者地址
    RCPT TO 指明的接收者地址
"""
