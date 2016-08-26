#coding=utf8
from textwrap import *


#使用textwrap中的方法
#wrap(text, width = 70, **kwargs):这个函数可以把一个字符串拆分成一个序列
#fill(text, width=70, **kwargs) :该方法可以根据指定的长度，进行拆分字符串，然后逐行显示
#dedent()方法->文本进行不缩进显示
#indent()方法->进行缩进显示

def test_wrap():
    test_str = '''\
    The textwrap module provides two convenience functions, wrap() and fill(), as well as 1
    TextWrapper, the class that does all the work, and two utility functions, dedent() and indent(). If 2
    you're just wrapping or filling one or two text strings, the convenience functions should be good 3
    enough; otherwise, you should use an instance of TextWrapper for efficiency. 4'''
    wstr = wrap(test_str, 20)
    print(type(wstr))
    print(wstr)
    print('\n\n')

    fstr = fill(test_str, 40)
    print(type(fstr))
    print(fstr)
    print('\n\n')

    dstr = dedent(test_str)
    print(type(dstr))
    print(dstr)
    print('\n')
    print(repr(dstr))




def main():
    test_wrap()



if __name__ == '__main__':
    main()
