#coding=utf8

def teste():
    sdf = (1 ,2 ,3)
    try:
        raise StopIteration
    except StopIteration:
        print 1111
        print sdf
    print 2222


if __name__ == '__main__':
    teste()
