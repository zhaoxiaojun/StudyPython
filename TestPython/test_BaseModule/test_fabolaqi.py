#coding=utf8


def feibolaqi(n):
    if n == 0 or n == 1:
        return n
    else:
        return feibolaqi(n-1) + feibolaqi(n-2)

num = int(raw_input('please input a int:'))
if num >= 0:
    print 'feibolaqi(%d) is %d' % (num,feibolaqi(num))
else:
    print 'input is wrong'
