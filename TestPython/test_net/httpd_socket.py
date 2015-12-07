#coding=UTF8
import socket
import re

HOST = '127.0.0.1'
PORT = 8001

#Read index.html, put into HTTP response data
index_content = '''
HTTP/1.x 200 ok
Content-Type: text/html

{'sdf':'dsgf'
'sdf':'sdfsdg'
'sdgsg': {
'1':'a'
'2':'b'
}
'sdfsfdf':'dsfgdsfg'
}
'''
#ffile = open('index.html', 'r')
#index_content += ffile.read()
#ffile.close()

#Read reg.html, put into HTTP response data
reg_content = '''
HTTP/1.x 200 ok
Content-Type: text/html

'''

ffile = open('reg.html', 'r')
reg_content += ffile.read()
ffile.close()

#Configure socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(100)   #最大连接数100
print 'sock: ',sock
#infinite loop
while True:
    # maximum number of requests waiting
    conn, addr = sock.accept()   #sock调用accept() 时，系统进入waiting状态，等待连接。有连接时，返回一个元组，元组中包含 connection （连接套接字）， address （连接地址）
    print 'conn: ',conn
    print 'addr: ',addr
    try:
        request = conn.recv(1024)  #必须加上每次接受的最大数据量，进入block状态，函数返回值为收到的数据字符串。如果想要发送如数组，字典这种数据结构，这可考虑使用 json 格式来进行数据转换发送。
        request_list = request.split(' ')
        print 'request_list: ', request_list
        method = request_list[0]
        src = request_list[1]
        print 'Connect by: ', addr
        print 'Request is:\n', request

        #deal wiht GET method
        if method == 'GET':
            if src == '/index.html':
                content = index_content
            elif src == '/reg.html':
                content = reg_content
            elif re.match('^/\?.*$', src):
                entry = src.split('?')[1]      # main content of the request
                content = 'HTTP/1.x 200 ok\r\nContent-Type: text/html\r\n\r\n'
                content += entry
                content += '<br /><font color="green" size="7">register successs!</p>'
            else:
                continue

        #deal with POST method
        elif method == 'POST':
            form = request.split('\r\n')
            entry = form[-1]      # main content of the request
            content = 'HTTP/1.x 200 ok\r\nContent-Type: text/html\r\n\r\n'
            content += entry
            content += '<br /><font color="green" size="7">register successs!</p>'
        else:
            continue
    except:
        print 'exception!'
        continue

    conn.sendall(content)
    #close connection
    conn.close()
    print '--------'
    print 'conn2: ',conn

    sock.close()
    print 'sock2: ',sock

