#coding=utf8
import logging
from Global import *
from test1 import testh

def test_logging():
    logger.debug('This is debug %s' % 'nnnnnn')
    logger.info('This is info message')
    logger.warning('This is warning %s' % 'mmmmmm')


if __name__ == '__main__':
    #logger
    logger.setLevel(logging.DEBUG)

    #handler
    logfile = logging.FileHandler("./Test_Tiancheng_log.txt")
    logfile.setLevel(logging.DEBUG)
    control = logging.StreamHandler()
    control.setLevel(logging.WARNING)


    #formatter
    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')
    logfile.setFormatter(formatter)
    control.setFormatter(formatter)

    #绑定
    logger.addHandler(control)
    logger.addHandler(logfile)

    test_logging()
    testh()
