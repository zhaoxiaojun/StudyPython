#coding=utf8

class A(object):
    def __init__(self):
        print("Enter A")
        print("Leave A")

class B(A):
    def __init__(self):
        print("Enter B")
        #super(B, self).__init__()
        A.__init__(self)
        print("Leave B")

class C(A):
    def __init__(self):
        print("Enter C")
        super(C, self).__init__()
        print("Leave C")

class D(A):
    def __init__(self):
        print("Enter D")
        super(D, self).__init__()
        print("Leave D")

class E(B, C, D):
    def __init__(self):
        print("Enter E")
        super(E, self).__init__()
        print("Leave E")


#在super机制里可以保证公共父类仅被执行一次，至于执行的顺序，是按照mro进行的
print E.__mro__

e = E()
#b = B()
