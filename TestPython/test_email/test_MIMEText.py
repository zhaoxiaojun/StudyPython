#coding=utf8
#建立MIMEText对象

from email.MIMEText import MIMEText
from email import Utils


message = '''Hello,
This is a test massage from test_MIMEText.py
'''

msg = MIMEText(message)
msg['From'] = 'yechaohui@tuandai.com'
msg['To'] = 'Test Sender <yechaohui@tuandai.com>'
msg['Subject'] = u'来自test_MIMEText.py的问候…'
msg['Date'] = Utils.formatdate(localtime = 1)  #产生当前日期时间
msg['Message-ID'] = Utils.make_msgid() #产生世界唯一的Message-ID


print msg.as_string()

'''
构造一个邮件对象就是一个Messag对象，如果构造一个MIMEText对象，就表示一个文本邮件对象，如果构造一个MIMEImage对象，就表示一个作为附件的图片，要把多个对象组合
起来，就用MIMEMultipart对象，而MIMEBase可以表示任何对象。它们的继承关系如下：
Message
+- MIMEBase
   +- MIMEMultipart
   +- MIMENonMultipart
      +- MIMEMessage
      +- MIMEText
      +- MIMEImage
'''
