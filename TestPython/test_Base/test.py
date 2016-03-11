#coding=utf8

class testc(object):
    def __init__(self, *args):
        self.sdf(*args)

    def sdf(self, *args):
        print args





if __name__ == '__main__':
    testcO = testc(1,2,3)

