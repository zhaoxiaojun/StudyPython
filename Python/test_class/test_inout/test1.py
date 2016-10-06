#coding=utf8


class sdf(object):

    class fds(object):   #内部类
        def aaa(self):
            print 'aaa'

    def www(self):
        fdsd = sdf.fds()  #类中方法实例化类中的另一个类(内部类)
        fdsd.aaa()
        print 'www'

sdfd = sdf()
sdfd.www()
