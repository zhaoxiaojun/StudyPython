#coding=utf8
#斐波那契数列

fibonacci = (lambda x, x1=1, x0=0: x0 if x == 0 else fibonacci(x-1, x1+x0, x1))

print fibonacci(1)

print fibonacci(5)

print fibonacci(6)




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
