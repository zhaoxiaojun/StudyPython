#coding=utf8
'''
pickle模块实现了基本的数据序列和反序列化。通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储；通过pickle模块的
反序列化操作，我们能够从文件中创建上一次程序保存的对象
'''
#作用：腌制数据
import pickle

try:
    with open('mydate.pickle', 'wb') as mysavedata:  #以二进制模式打开文件
        pickle.dump([1,2,'three'], mysavedata)   #数据被腌制存到文件中
except IOError as err:
    print('error: ' + str(err))
except pickleError as perr:
    print('error: ' + str(perr))



try:
    with open('mydate.pickle', 'rb') as mysavedata:  #读取文件中腌制的数据
        a_list = pickle.load(mysavedata)
    print a_list
except IOError as err:
    print('error: ' + str(err))
except pickleError as perr:
    print('error: ' + str(perr))


