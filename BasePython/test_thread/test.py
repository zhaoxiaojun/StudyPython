#coding=utf8
import threading, multiprocessing
import time

'''
def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):  #multiprocessing.cpu_count(): CPU个数
    t = threading.Thread(target=loop)
    t.start()
'''

class MyThread(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(5)
        print "This is " + self.getName()

if __name__ == "__main__":
    t1=MyThread(999)
    t1.setDaemon(False)   #setDaemon的默认值是False
    t1.start()
    print "I am the father thread."
