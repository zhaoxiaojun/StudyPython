#coding=utf8
import logging
import time

def ch2debug(data):
    return unicode(data).encode('utf-8')

def ch2release(data):
    return unicode(data).encode('gbk')

def ch2unicode(data):
    '''
    转换为unicode
    '''
    if type(data) is unicode:
        return data
    if type(data) is not str:
        data = str(data)
    try:
        data = unicode(data, 'utf-8')
    except UnicodeDecodeError:
        data = unicode(data, 'gbk')
    return data


def testprint(level, fixd, *data):
    if level == 'exception':
        getattr(logger1, level)(fixd)
        getattr(logger2, level)(fixd)
    else:
        fixd = ch2unicode(fixd).encode('utf-8')
        values = []
        for d in data:
            d = ch2unicode(d).encode('utf-8')
            values.append(d)
        print fixd
        print values
        print tuple(values)
        #values = ('This is debug中文繁體','sdfsdfsaf中文繁體')
        getattr(logger1, level)(fixd % tuple(values))
        getattr(logger2, level)(fixd % tuple(values))


logger1 = logging.getLogger('1')
logger2 = logging.getLogger('2')

logger1.setLevel(logging.DEBUG)
logger2.setLevel(logging.DEBUG)
'''
默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别
'''

#handler
logfile = logging.FileHandler("./Test_Tiancheng_logtest2.txt")
logfile.setLevel(logging.DEBUG)

control = logging.StreamHandler()
control.setLevel(logging.DEBUG)


#formatter
#formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logfile.setFormatter(formatter)
control.setFormatter(formatter)


#绑定
logger1.addHandler(logfile)
logger2.addHandler(control)

#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S')


data = 4545.0

logger2.debug('%s - %s sdfsdlfksfksdfksf', 'finename', 'lineN')
#logger2.info('This is info message')
#logger2.warning('This is warning %s' % 'mmmmmm')
#try:
#    a = 1 / 0
#except Exception as e:
#    print repr(e)
#    testprint('debug', 'exccc: %s', repr(e))

