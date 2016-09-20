#coding=utf-8
from time import sleep, ctime
import threading

def muisc(data_mic):
    for i in range(2):
        print 'Start playing: %s! %s' %(data_mic,ctime())
        sleep(2)

def move(data_mov):
    for i in range(2):
        print 'Start playing: %s! %s' %(data_mov,ctime())
        sleep(5)


#判断文件类型，交给相应的函数执行
def player(name):
    r = name.split('.')[1]
    if r == 'mp3':
        muisc(name)
    elif r == 'mp4':
        move(name)
    else:
        print 'error: The format is not recognized!'

data_list = [u'爱情买卖.mp3',u'阿凡达.mp4'] 


threads = []

files = range(len(data_list))
#创建线程
for i in files:
    t = threading.Thread(target=player,args=(data_list[i],))
    threads.append(t)


if __name__ == '__main__':
    #启动线程
    for i in files:
        threads[i].start()
    
    for i in files:
        threads[i].join()
#主线程
print 'end:%s' %ctime()
