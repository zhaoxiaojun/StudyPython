#coding=utf8
'''
做题
'''

def Fizz(one, two, three):
    onestr = 'Fizz'
    twostr = 'Buzz'
    threestr = 'Whizz'
    for i in xrange(1,101):
        istr = ''
        for x in str(i):
            if one == int(x):
                istr = onestr
                break
        if istr:
            print istr
            continue
        n = 0
        if i % one == 0:
            n += 100
        if i % two == 0:
            n += 10
        if i % three == 0:
            n += 1
        istr = onestr*(n/100) + twostr*(n%100/10) + threestr*(n%100%10/1)
        if istr:
            print istr
        else:
            print i


Fizz(3,5,7)
