#coding=utf8
from email import encoders
from email.header import Header
#from email.mime.text import MIMEText
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib
'''
发送带附件的邮件
'''

def _format_addr(s):   #格式化一个邮件地址
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))  #.. if .. else .. 结构

from_addr = 'yzh87117835@163.com'
password = 'mC7uE5wJ_8528'
to_addr = 'yechaohui@tuandai.com'
smtp_server = 'smtp.163.com'

msg = MIMEMultipart() #MIMEMultipart对象代表邮件本身
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

#邮件正文是MIMEText:
#msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

'''
把一个图片嵌入到邮件正文中
'''
#大部分邮件服务商都会自动屏蔽带有外链的图片，因为不知道这些链接是否指向恶意网站。要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，
#先把邮件作为附件添加进去，然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))


#添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('test.jpg', 'rb') as f:
    #设置附件的MIME和文件名，这里是jpg类型:
    mime = MIMEBase('image', 'jpg', filename='test.jpg')
    #加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    #把附件的内容读进来:
    mime.set_payload(f.read())
    #用Base64编码:
    encoders.encode_base64(mime)
    #添加到MIMEMultipart:
    msg.attach(mime)


server = smtplib.SMTP(smtp_server, 25)  #SMTP协议默认端口是25
#server.set_debuglevel(1)  #打印出和SMTP服务器交互的所有信息
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())  #可以一次发给多个人
server.quit()



