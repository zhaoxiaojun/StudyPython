#coding=utf8
import time

class SalesManager(object):
    def work(self):
        print("Sales Manager working...")

    def talk(self):
        print("Sales Manager ready to talk")


class Proxy(object):
    def __init__(self):
        self.busy = 'No'
        self.sales = None

    def work(self):
        print("Proxy checking for Sales Manager availability")
        if self.busy == 'No':
            self.sales = SalesManager()
            time.sleep(2)
            self.sales.talk()
        else:
            time.sleep(2)
            print("Sales Manager is busy")


class NoTalkProxy(Proxy):
    def __init__(self):
        Proxy.__init__(self)

    def work(self):
        print("Proxy checking for Sales Manager availability")
        time.sleep(2)
        print("This Sales Manager will not talk to you whether he/she is busy or not")


if __name__ == '__main__':
    p = Proxy()
    p.work()
    print '\n----------------\n'

    p.busy = 'Yes'
    p.work()
    print '\n----------------\n'

    p = NoTalkProxy()
    p.work()
    print '\n----------------\n'

    p.busy = 'Yes'
    p.work()
