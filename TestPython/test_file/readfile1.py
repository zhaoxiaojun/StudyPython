#coding=utf8

try:
    fp = open('test.txt', 'r')
    line = fp.readline()
    print line
except IOError as err:
    print('error: ' + str(err))
finally:
    fp.close()



