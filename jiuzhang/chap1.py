#coding=utf8

#reverse 3-digit integer
def reverse3bitNum(Num):
    g = Num % 10
    s = Num / 10 % 10
    b = Num / 100
    return g*100+s*10+b

#exchange two integers
def exchange2Num(a ,b):
    a, b = b, a
    return a, b



if __name__ == '__main__':
    Num = 123
    print(reverse3bitNum(Num))

    a = 123
    b = 876
    print(exchange2Num(a,b))

