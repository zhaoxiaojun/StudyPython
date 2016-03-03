#coding=utf8
#建立MIMEMultipart对象
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import Utils, Encoders

def alternative(data, contenttype):
    maintype, subtype = contenttype.split('/')
    if maintype == 'text':
        retval = MIMEText(data, _subtype=subtype)
    else:
        retval = MIMEBase(maintype, subtype)
        retval.set_payload(data)
        Encoders.encode_base64(retval)
    return retval


messagetext = '''Hello,
This is a test massage from test_MIMEText.py
'''

messagehtml = '''<html><body><h1>Hello</h1>
<p>send by <a href="http://www.python.org">Python</a>...</p>
</body></html>'''


msg = MIMEMultipart('alternative')
msg['From'] = 'yechaohui@tuandai.com'
msg['To'] = 'Test Sender <yechaohui@tuandai.com>'
msg['Subject'] = u'来自test_MIMEText.py的问候…'
msg['Date'] = Utils.formatdate(localtime = 1)
msg['Message-ID'] = Utils.make_msgid()


msg.attach(alternative(messagetext, 'text/plain'))
msg.attach(alternative(messagehtml, 'text/html'))
print msg.as_string()

