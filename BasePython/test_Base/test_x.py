#coding=utf8

def print_three_thing(a, b, c):
    print 'a={0}, b={1}, c={2}'.format(a, b, c)

mylist = ['asdfsds','bsdbsds','cftyxcf']
print_three_thing(*mylist)  #函数调用时使用*号
