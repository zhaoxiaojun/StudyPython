#coding=utf-8
from time import sleep, ctime
import threading

#创建超级播放器
def super_player(mp_file,mp_time):
    for i in range(2):
        print 'Start playing: %s! %s' %(mp_file,ctime())
        sleep(mp_time)


#播放的文件和播放时长
data_list = {u'爱情买卖.mp3':3,u'阿凡达.mp4':5,u'我和你.mp3':4}

threads = []
files = range(len(data_list))

#创建线程
for mp_file,mp_time in data_list.items():
    t = threading.Thread(target=super_player,args=(mp_file,mp_time))
    threads.append(t)


if __name__ == '__main__':
    #启动线程
    for i in files:
        threads[i].start()

    for i in files:
        threads[i].join()

#主线程
print 'end:%s' %ctime()
