#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def check_contain_chinese(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

if __name__ == '__main__':
    print check_contain_chinese(u'sdf中文sdfsd')
