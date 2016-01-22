#coding=utf-8
#演示正则表达式
import re

def test_short():
    q = re.search('\d\d','Data (21 bytes)')
    print q.group(0)
    
    p = re.match(r'Data \((.*) bytes\)', 'Data (21 bytes)')
    print p.groups()

    '''
            其他写法：
    target = 'Data (21 bytes)'
    p = re.compile(r'Data \((.*) bytes\)')
    print p.match(target).groups()
    ''' 

def test_long():
    target = '''
Data(21 bytes)
aaaaaaaaaaa
bbbbbbbbbbbbbbbbbb
Data(22 bytes)
cccc
dddddddddddddddd
'''
    p = re.match('\nData\((.*) bytes\)\n(.*)\n(.*)\nData\((.*) bytes\)\n(.*)\n(.*)\n', target)
    print p.groups()
    
    '''
             其他写法：
    p = re.compile('\nData\((.*) bytes\)\n(.*)\n(.*)\nData\((.*) bytes\)\n(.*)\n(.*)\n')
    print p.match(target).groups()
    '''
if __name__ == '__main__':
    test_short()
    test_long()