#coding=utf8
#腌制数据
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


