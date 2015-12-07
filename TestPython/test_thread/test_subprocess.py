#coding=utf8
import subprocess

#print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
#print type(r)
#print('Exit code:', r)
