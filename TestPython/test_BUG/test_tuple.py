#coding=utf8
tup = ([],)

try:
    tup[0] = tup[0] + [1]
except Exception as e:
    print e
    print tup

try:
    tup[0] += [1]
except Exception as e:
    print e
    print tup
'''
OMG! +=不是先+后=吗，为啥结果不一样？ 第二个赋值不是产生异常了吗，为啥结果还赋值成功了？
'''


my_tup = (1,)
print my_tup
print(id(my_tup))

my_tup += (4,)
print my_tup
print(id(my_tup))

my_tup = my_tup + (5,)
print my_tup
print(id(my_tup))
'''
答案：操作的不是原来的元组
'''
