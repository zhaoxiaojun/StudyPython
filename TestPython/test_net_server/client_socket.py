#coding=utf8
import socket,sys

host = "www.51testing.com"
port = 80

try:
    scon = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scon.connect((host, port))
except (socket.error, socket.herror), e:
    print "Connect is error, Exception is %s" % str(e)
    sys.exit()
except socket.timeout, e:
    print "Socket timeout, Exception is %s" % str(e)
    sys.exit()

print "con from ", scon.getsockname()
print "con to ", scon.getpeername()

scon.shutdown(1)

scon.sendall("111111111111\r\n")






    
    
