#coding=utf8
#from ggg import *
import ggg
import threading
import time


class mmm(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        #global ggg.isflag
        print 'mmm isflag id: ', id(ggg.isflag)
        print 'mmm isflag: ', ggg.isflag

        while not ggg.isflag:
            print 'mmm isflag id: ', id(ggg.isflag)
            print 'mmm isflag: ', ggg.isflag
            print 'sleep...\n'
            time.sleep(0.5)
            print 'sleep end\n'
